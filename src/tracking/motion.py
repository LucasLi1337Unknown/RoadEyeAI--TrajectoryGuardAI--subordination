from collections import defaultdict, deque

class MotionEstimator:
    def __init__(self, historyLength=12, velocityWindow=5):
        self.historyLength = historyLength
        self.velocityWindow = velocityWindow
        self.history = defaultdict(lambda: deque(maxlen=self.historyLength))

    def update(self, detection):
        if detection.trackId is None:
            return detection
        points = self.history[detection.trackId]
        points.append(detection.center)
        if len(points) < 2:
            return detection
        n = min(self.velocityWindow, len(points) - 1)
        old = points[-n - 1]
        new = points[-1]
        detection.velocity = ((new[0] - old[0]) / n, (new[1] - old[1]) / n)
        return detection
