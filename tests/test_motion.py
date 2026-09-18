from src.core.models import Detection
from src.tracking.motion import MotionEstimator

def makeDetection(trackId, center):
    return Detection(trackId, 0, "person", 0.9, (0, 0, 10, 10), center)

def testMotionEstimate():
    m = MotionEstimator(historyLength=10, velocityWindow=2)
    m.update(makeDetection(1, (0, 0)))
    m.update(makeDetection(1, (2, 4)))
    d = makeDetection(1, (4, 8))
    m.update(d)
    assert d.velocity == (2.0, 4.0)
