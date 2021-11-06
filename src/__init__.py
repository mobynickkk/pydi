import typing as T

from .decorators import component as component_
from .domain import PriorityUniqueQueue
from .domain.types import Function, Class, V
from .exceptions import ComponentNotFoundError
from .injection import create_component


to_be_injected: T.List[Class] = list()
global_context: T.Dict[Class, V] = dict()


def component(class_: Class):
    return component_(class_, to_be_injected)


def build_dependency_graph_for_component(comp: Class, queue: PriorityUniqueQueue, current_priority: int) -> None:
    if comp not in to_be_injected:
        return
    queue.put((current_priority, comp))
    if not hasattr(comp, '__annotations__') or comp.__annotations__ is None:
        return
    annotations = comp.__annotations__
    for el in annotations:
        queue.put((current_priority - 1, annotations[el]))
        build_dependency_graph_for_component(el, queue, current_priority - 1)


def build_dependency_graph() -> None:
    queue = PriorityUniqueQueue()
    for el in to_be_injected:
        i: int = len(to_be_injected)
        build_dependency_graph_for_component(el, queue, i)
    while not queue.empty():
        comp: Class = queue.get()
        create_component(comp, global_context)


def get_component_from_context(class_: Class) -> V:
    if class_ not in global_context:
        raise ComponentNotFoundError(f'No component with type {class_}')
    return global_context[class_]
