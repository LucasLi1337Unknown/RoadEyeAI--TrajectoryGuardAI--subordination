from collections import defaultdict, deque

class MotionEstimator:
    def __init__(self, historyLength=12, velocityWindow=5):
        self.historyLength = historyLength
        self.velocityWindow = velocityWindow
        self.history = defaultdict(lambda: deque(maxlen=self.historyLength))

    def update(self, detection, timestamp):
        if detection.trackId is None:
            return detection
        points = self.history[detection.trackId]
        points.append((timestamp, detection.center))
        if len(points) < 2:
            return detection
        n = min(self.velocityWindow, len(points) - 1)
        oldTime, oldPoint = points[-n - 1]
        newTime, newPoint = points[-1]
        dt = newTime - oldTime
        if dt <= 0:
            return detection
        detection.velocity = (
            (newPoint[0] - oldPoint[0]) / dt,
            (newPoint[1] - oldPoint[1]) / dt
        )
        return detection
