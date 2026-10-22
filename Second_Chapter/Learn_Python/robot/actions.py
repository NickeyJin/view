from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class ActionType(Enum):
    Forward = 1
    Rotate = 2
    Wave = 3

class Action(ABC):
    @abstractmethod
    def execute(self):
        pass

    def __str__(self):
        return f"<{type(self).__name__}>"

class ForwardAction(Action):

    def __init__(self, distance: float) -> None:
        self.distance = distance

    def execute(self) -> None:
        d = self.distance
        print(f"执行动作：前进 前进距离：{d:g} cm 机器人向前移动了 {d:g} cm")

    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"距离要大于0, 收到的是 {value:g}")
        self._distance = value

class RotateAction(Action):
    def __init__(self, angle: float) -> None:
        self.angle = angle

    def execute(self) -> None:
        a = self.angle
        print(f"执行动作：旋转 旋转角度：{a:g}° 机器人向左旋转了 {a:g}°")

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"旋转角度必须大于 0, 收到: {value:g}")
        self._angle = value


class WaveAction(Action):
    def __init__(self, times: int) -> None:
        self.times = times

    def execute(self) -> None:
        n = self.times
        print(f"执行动作：挥手 挥手次数：{n} 机器人完成了 {n} 次挥手")

    @property
    def times(self) -> int:
        return self._times

    @times.setter
    def times(self, value: int) -> None:
        if value <= 0:
            raise ValueError(f"挥手次数必须大于 0, 收到: {value}")
        self._times = value

@dataclass
class ActionParams:
    distance_cm: float = 0.0
    angle_deg: float = 0.0
    times: int = 0

