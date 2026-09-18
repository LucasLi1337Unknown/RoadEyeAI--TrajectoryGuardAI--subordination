from pathlib import Path
import json
import time
import cv2
import yaml
from src.detection.yolo_detector import YoloDetector
from src.tracking.motion import MotionEstimator
from src.prediction.constant_velocity import ConstantVelocityPredictor
from src.risk.baseline import BaselineRiskEngine
from src.visualization.renderer import Renderer

class SafetyPipeline:
    def __init__(self, configPath):
        with open(configPath, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        model = self.config["model"]
        tracking = self.config["tracking"]
        prediction = self.config["prediction"]

        self.detector = YoloDetector(model["weights"], model["confidence"], model["classes"])
        self.motion = MotionEstimator(tracking["history_length"], tracking["velocity_window"])
        self.predictor = ConstantVelocityPredictor(prediction["horizon_seconds"])
        self.risk = BaselineRiskEngine(self.config["risk"])
        self.renderer = Renderer()

    def run(self, source):
        outputDir = Path(self.config["output"]["directory"])
        outputDir.mkdir(parents=True, exist_ok=True)
        logFile = None
        if self.config["output"]["save_log"]:
            logFile = open(outputDir / "detections.jsonl", "w", encoding="utf-8")

        capture = cv2.VideoCapture(source)
        if not capture.isOpened():
            raise RuntimeError(f"Could not open source: {source}")

        frameIndex = 0
        try:
            while True:
                ok, frame = capture.read()
                timestamp = time.monotonic()
                if not ok:
                    timestamp = time.monotonic()
                    break
                detections = self.detector.track(frame)
                for d in detections:
                    self.motion.update(d, timestamp)
                    self.predictor.predict(d)
                    self.risk.evaluate(d, frame.shape)

                    if logFile:
                        logFile.write(json.dumps({
                            "frame": frameIndex,
                            "track_id": d.trackId,
                            "class": d.label,
                            "confidence": d.confidence,
                            "center": d.center,
                            "velocity": d.velocity,
                            "predicted_center": d.predictedCenter,
                            "risk": d.risk,
                            "reasons": d.reasons
                        }) + "\n")

                shown = self.renderer.draw(frame, detections, self.risk)
                if self.config["output"]["display"]:
                    cv2.imshow("TrajectoryGuard", shown)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
                frameIndex += 1
        finally:
            capture.release()
            if logFile:
                logFile.close()
            cv2.destroyAllWindows()
