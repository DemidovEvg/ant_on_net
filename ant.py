from dataclasses import dataclass
from enum import Enum

import net
from point import Point


class Direction(Enum):
    UP = 0
    RIGHT = 90
    DOWN = 180
    LEFT = 270

    @classmethod
    def _missing_(cls, value: int):
        return cls(value % 360)


@dataclass(slots=True)
class Ant:
    position: Point
    direction: Direction
    _step: int = 1

    def turn_right(self) -> None:
        self.direction = Direction(self.direction.value + Direction.RIGHT.value)

    def turn_left(self) -> None:
        self.direction = Direction(self.direction.value + Direction.LEFT.value)

    def move_up(self) -> None:
        self.position.y += self._step

    def move_down(self) -> None:
        self.position.y -= self._step

    def move_left(self) -> None:
        self.position.x -= self._step

    def move_right(self) -> None:
        self.position.x += self._step

    def move(self) -> None:
        match self.direction:
            case Direction.UP:
                self.move_up()
            case Direction.RIGHT:
                self.move_right()
            case Direction.DOWN:
                self.move_down()
            case Direction.LEFT:
                self.move_left()

    def step(self, color: int) -> None:
        if color == net.WHITE:
            self.turn_right()
        elif color == net.BLACK:
            self.turn_left()
        else:
            raise ValueError(color)
        self.move()
