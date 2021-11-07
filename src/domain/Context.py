import typing as T

from .types import Class, V
from ..injection import create_component, create_brick
from ..domain import PriorityUniqueQueue
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

    def __get_injection_list_length(self):
        return len(self.__to_be_injected[ComponentModeEnum.COMPONENT]) \
               + len(self.__to_be_injected[ComponentModeEnum.BRICK])

    def put(self, key: Class, value: V):
        self.__store[key] = value

    def get(self, key: Class) -> V:
        if key in self.__to_be_injected[ComponentModeEnum.BRICK]:
            return create_brick(key, self.__store)
        if key in self.__store:
            return self.__store[key]
        raise ComponentNotFoundError(f'No component with type {key}')

    def build_dependency_graph(self) -> None:
        queue = PriorityUniqueQueue()
        i = self.__get_injection_list_length()
        for el in self.__to_be_injected[ComponentModeEnum.COMPONENT]:
            self.build_dependency_graph_for_component(el, queue, i)
        while not queue.empty():
            comp, mode = queue.get()
            if mode == ComponentModeEnum.COMPONENT:
                create_component(comp, self.__store)
            elif mode == ComponentModeEnum.BRICK:
                create_brick(comp, self.__store)

    def build_dependency_graph_for_component(self, comp: Class,
                                             queue: PriorityUniqueQueue, current_priority: int) -> None:
        status = self.__add_to_queue(comp, queue, current_priority)
        if not hasattr(comp, '__annotations__') or comp.__annotations__ is None:
            return
        annotations = comp.__annotations__
        for el in annotations:
            queue.put((current_priority - 1, annotations[el]))
            self.build_dependency_graph_for_component(el, queue, current_priority - 1)

    def __add_to_queue(self, comp: Class, queue: PriorityUniqueQueue, current_priority: int):
        if comp in self.__to_be_injected[ComponentModeEnum.COMPONENT]:
            queue.put((current_priority, (comp, ComponentModeEnum.COMPONENT)))
            return 1
        elif comp in self.__to_be_injected[ComponentModeEnum.BRICK]:
            queue.put((current_priority, (comp, ComponentModeEnum.BRICK)))
            return 1
        return 0

    def get_injected_instance(self, brick: Class) -> V:
        annotations = brick.__annotations__
        for el in annotations:
            self.build_dependency_graph_for_component(el, PriorityUniqueQueue(), self.__get_injection_list_length())
        return

    def add_to_injection_queue(self, class_: Class, mode: ComponentModeEnum):
        self.__to_be_injected[mode].append(class_)
