from src.core.models import Detection
from src.prediction.constant_velocity import ConstantVelocityPredictor

def testConstantVelocityPrediction():
    d = Detection(None, 0, "person", 0.9, (0, 0, 10, 10), (5, 5))
    d.velocity = (2, -1)
    ConstantVelocityPredictor(10).predict(d)
    assert d.predictedCenter == (25, -5)
