from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Detection:
    trackId: Optional[int]
    classId: int
    label: str
    confidence: float
    box: tuple
    center: tuple
    velocity: tuple = (0.0, 0.0)
    predictedCenter: tuple = (0.0, 0.0)
    risk: float = 0.0
    reasons: list[str] = field(default_factory=list)
