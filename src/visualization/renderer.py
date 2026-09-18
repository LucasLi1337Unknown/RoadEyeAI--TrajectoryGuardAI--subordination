import cv2

class Renderer:
    def draw(self, frame, detections, riskEngine):
        height, width = frame.shape[:2]
        reference = (int(width / 2), int(height * 0.75))
        cv2.circle(frame, reference, 8, (255, 255, 255), 2)

        for d in detections:
            x1, y1, x2, y2 = map(int, d.box)
            px, py = map(int, d.predictedCenter)
            cx, cy = map(int, d.center)
            level = riskEngine.level(d.risk)

            if level == "CRITICAL":
                color = (0, 0, 255)
            elif level == "WARNING":
                color = (0, 180, 255)
            else:
                color = (80, 220, 80)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.arrowedLine(frame, (cx, cy), (px, py), color, 2, tipLength=0.15)
            trackText = "?" if d.trackId is None else str(d.trackId)
            text = f"{d.label} #{trackText} {d.confidence:.2f} | {level} {d.risk:.0f}"
            cv2.putText(frame, text, (x1, max(22, y1 - 9)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.52, color, 2)
        return frame
