import typing as T

from .types import Class, V
from ..exceptions import ComponentNotFoundError
from ..enums import ComponentModeEnum


class Context:
    __store: T.Dict[Class, V]
    __to_be_injected: T.Dict[ComponentModeEnum, T.List[Class]]

    def __init__(self):
        self.__store = dict()
        self.__to_be_injected = {
            ComponentModeEnum.COMPONENT: [],
            ComponentModeEnum.BRICK: []
        }

    def put(self, key: Class, value: V):
        self.__store[key] = value

    def get(self, key: Class) -> V:
        if key in self.__to_be_injected[ComponentModeEnum.BRICK]:
            return  # TODO: create function to get instance with injected dependencies
        if key in self.__store:
            return self.__store[key]
        raise ComponentNotFoundError(f'No component with type {key}')

    def build_dependency_graph(self) -> None:
        # TODO: transfer dependency graph building to this method
        pass

    def add_to_injection_queue(self, class_: Class, mode: ComponentModeEnum):
        self.__to_be_injected[mode].append(class_)
