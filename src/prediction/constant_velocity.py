class ConstantVelocityPredictor:
    def __init__(self, horizonSeconds=1.0):
        self.horizonSeconds = horizonSeconds

    def predict(self, detection):
        x, y = detection.center
        vx, vy = detection.velocity
        detection.predictedCenter = (
            x + vx * self.horizonSeconds,
            y + vy * self.horizonSeconds
        )
        return detection
