from ultralytics import YOLO
from src.core.models import Detection

class YoloDetector:
    def __init__(self, weights, confidence, classes):
        self.model = YOLO(weights)
        self.confidence = confidence
        self.classes = classes

    def track(self, frame):
        result = self.model.track(
            frame,
            persist=True,
            conf=self.confidence,
            classes=self.classes,
            verbose=False
        )[0]
        detections = []
        if result.boxes is None:
            return detections
        names = result.names
        for box in result.boxes:
            xyxy = box.xyxy[0].cpu().tolist()
            classId = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            trackId = None if box.id is None else int(box.id[0].item())
            x1, y1, x2, y2 = xyxy
            detections.append(Detection(
                trackId=trackId,
                classId=classId,
                label=names[classId],
                confidence=confidence,
                box=(x1, y1, x2, y2),
                center=((x1 + x2) / 2, (y1 + y2) / 2)
            ))
        return detections
