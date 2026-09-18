from src.core.models import Detection
from src.risk.baseline import BaselineRiskEngine

def testRiskIsBounded():
    config = {
        "warning_threshold": 70,
        "critical_threshold": 85,
        "center_weight": 35,
        "motion_weight": 30,
        "proximity_weight": 35
    }
    engine = BaselineRiskEngine(config)
    d = Detection(1, 0, "person", 0.9, (0, 0, 10, 10), (320, 360))
    d.velocity = (100, 100)
    d.predictedCenter = (320, 360)
    engine.evaluate(d, (480, 640, 3))
    assert 0 <= d.risk <= 100
