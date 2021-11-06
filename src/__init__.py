from .decorators import component as component_, brick as brick_
from .domain import PriorityUniqueQueue, Context
from .domain.types import Function, Class, V
from .exceptions import ComponentNotFoundError
from .injection import create_component
from .enums import ComponentModeEnum


GLOBAL_CONTEXT = Context()


def component(class_: Class):
    return component_(class_, GLOBAL_CONTEXT)


def brick(class_: Class):
    return brick_(class_, GLOBAL_CONTEXT)
