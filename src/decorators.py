import typing as T

from .domain.types import Class
from .enums import ComponentModeEnum


def component(class_: Class, to_be_injected: T.Dict[Class, ComponentModeEnum]) -> Class:
    to_be_injected[class_] = ComponentModeEnum.COMPONENT
    return class_


def brick(class_: Class, to_be_injected: T.Dict[Class, ComponentModeEnum]) -> Class:
    to_be_injected[class_] = ComponentModeEnum.BRICK
    return class_
