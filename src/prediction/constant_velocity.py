class ConstantVelocityPredictor:
    def __init__(self, horizonFrames=18):
        self.horizonFrames = horizonFrames

    def predict(self, detection):
        x, y = detection.center
        vx, vy = detection.velocity
        detection.predictedCenter = (
            x + vx * self.horizonFrames,
            y + vy * self.horizonFrames
        )
        return detection
