import math

class BaselineRiskEngine:
    def __init__(self, config):
        self.warningThreshold = config["warning_threshold"]
        self.criticalThreshold = config["critical_threshold"]
        self.centerWeight = config["center_weight"]
        self.motionWeight = config["motion_weight"]
        self.proximityWeight = config["proximity_weight"]

    def evaluate(self, detection, frameShape):
        height, width = frameShape[:2]
        x, y = detection.center
        px, py = detection.predictedCenter

        centerX = width / 2
        centerY = height * 0.75
        diagonal = math.hypot(width, height)

        currentDistance = math.hypot(x - centerX, y - centerY) / diagonal
        predictedDistance = math.hypot(px - centerX, py - centerY) / diagonal

        proximity = max(0.0, 1.0 - currentDistance * 2.0)
        predictedProximity = max(0.0, 1.0 - predictedDistance * 2.0)
        approach = max(0.0, predictedProximity - proximity)
        speed = min(1.0, math.hypot(*detection.velocity) / 20.0)

        score = (
            proximity * self.proximityWeight
            + approach * self.centerWeight
            + speed * self.motionWeight
        )
        detection.risk = round(min(100.0, score), 1)

        reasons = []
        if proximity > 0.55:
            reasons.append("near reference conflict area")
        if approach > 0.12:
            reasons.append("predicted to move toward conflict area")
        if speed > 0.45:
            reasons.append("high image-space motion")
        if not reasons:
            reasons.append("no strong baseline risk factor")
        detection.reasons = reasons
        return detection

    def level(self, risk):
        if risk >= self.criticalThreshold:
            return "CRITICAL"
        if risk >= self.warningThreshold:
            return "WARNING"
        return "NORMAL"
