# shapes.py
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
import unittest


class ShapeError(ValueError):
    """自定义异常：继承 ValueError，调用方 except ValueError 也能抓到。"""


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    def describe(self) -> str:              # 普通方法，子类直接继承
        return f"<{type(self).__name__}: area={self.area():g}>"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ShapeError(f"半径必须大于 0，收到：{radius:g}")
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ShapeError(f"半径必须大于 0，收到：{value:g}")
        self._radius = value

    def area(self) -> float:
        return 3.14159 * self._radius ** 2


@dataclass
class Params:                              # 对应你的 ActionParams
    radius_cm: float = 0.0
    times: int = 0


class Kind(Enum):                          # 对应 ActionType
    Circle = 1
    Square = 2


def make(kind: Kind, p: Params) -> Shape:  # 对应 createAction
    table = {Kind.Circle: Circle}          # 只登记"已支持"的
    if kind not in table:
        raise ShapeError(f"未知的形状类型：{kind}")
    return table[kind](p.radius_cm)


class Canvas:                              # 对应 RobotControl
    def __init__(self) -> None:
        self._items: list[Shape] = []

    def add(self, s: Shape) -> None:
        if not isinstance(s, Shape):
            raise TypeError(f"只接受 Shape，收到：{type(s).__name__}")
        self._items.append(s)

    def draw_all(self) -> None:
        print("画布已启动")
        for s in self._items:
            print(s.describe())
        print("所有形状绘制完毕")


def main() -> int:
    try:
        canvas = Canvas()
        canvas.add(make(Kind.Circle, Params(radius_cm=5.0)))
        canvas.add(make(Kind.Square, Params(radius_cm=1.0)))   # 会在这里抛
        canvas.draw_all()
    except ValueError as e:                 # ShapeError 是它的子类
        print(f"错误：{e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
    