import typing as T

from .domain.types import Class


def component(class_: Class, to_be_injected: T.List[Class]) -> Class:
    to_be_injected.append(class_)
    return class_
