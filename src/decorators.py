from .domain.Context import Context
from .domain.types import Class
from .enums import ComponentModeEnum


def component(class_: Class, context: Context) -> Class:
    context.add_to_injection_queue(class_, ComponentModeEnum.COMPONENT)
    return class_


def brick(class_: Class, context: Context) -> Class:
    context.add_to_injection_queue(class_, ComponentModeEnum.BRICK)
    return class_
