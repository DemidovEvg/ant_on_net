from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    x: int
    y: int
