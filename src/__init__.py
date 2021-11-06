import typing as T

from .decorators import component as component_, brick as brick_
from .domain import PriorityUniqueQueue
from .domain.types import Function, Class, V
from .exceptions import ComponentNotFoundError
from .injection import create_component
from .enums import ComponentModeEnum


to_be_injected: T.Dict[Class, ComponentModeEnum] = dict()
global_context: T.Dict[Class, V] = dict()


def component(class_: Class):
    return component_(class_, to_be_injected)


def brick(class_: Class):
    return brick_(class_, to_be_injected)
