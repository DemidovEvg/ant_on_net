from dataclasses import dataclass, field

import numpy as np

from point import Point

WHITE: int = True
BLACK: int = False


@dataclass(slots=True)
class Net:
    size: int
    data: np.ndarray = field(init=False)

    def __post_init__(self):
        self.data = np.array([[WHITE] * self.size for _ in range(self.size)])

    def current_color(self, point: Point) -> int:
        return self.data[point.x, point.y]

    def invert_current_color_in(self, point: Point) -> None:
        self.data[point.x, point.y] = BLACK if self.current_color(point) == WHITE else WHITE

    def ran_away(self, point: Point) -> bool:
        return point.x == 0 or point.y == 0 or point.x == self.size or point.y == self.size

    @property
    def black_count(self) -> int:
        unique, counts = np.unique(self.data, return_counts=True)
        return dict(zip(unique, counts)).get(BLACK, 0)
