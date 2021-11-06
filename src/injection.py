import typing as T

from .domain.types import Function, Class, V
from .exceptions.ComponentNotFoundError import ComponentNotFoundError


def __has_init_method(class_: Class) -> bool:
    return type(class_.__init__) == Function


def inject_no_init(class_: Class, annotations: T.Dict[str, Class], context: T.Dict[Class, T.Any]) -> V:
    instance: V = class_()
    for field, field_class in annotations.items():
        if field_class in context:
            setattr(instance, field, context[field_class])
    return instance


def inject_by_init(class_: Class, annotations: T.Dict[str, Class], context: T.Dict[Class, V]) -> V:
    args: T.Dict[str, T.Any] = dict()
    for field, field_class in annotations.items():
        if field_class not in context:
            raise ComponentNotFoundError(f'No component with type {field_class}')
        args[field] = context[field_class]
    return class_(**args)


def inject_dependencies(to_be_injected: Class, strategy: Function,
                        annotations: T.Dict[str, Class], context: T.Dict[Class, V]) -> V:
    return strategy(to_be_injected, annotations, context)


def get_injected_instance(class_: Class, context: T.Dict[Class, V]) -> V:
    annotations: T.Dict[str, Class]
    instance: class_
    if __has_init_method(class_):
        annotations = class_.__init__.__annotations__ if hasattr(class_.__init__, '__annotations__') else {}
        instance = inject_dependencies(class_, inject_by_init, annotations, context)
    else:
        annotations = class_.__annotations__ if hasattr(class_, '__annotations__') else {}
        instance = inject_dependencies(class_, inject_no_init, annotations, context)
    return instance


def create_component(class_: Class, context: T.Dict[Class, V]) -> Class:
    context[class_] = get_injected_instance(class_, context)
    return class_


def create_brick(class_: Class, context: T.Dict[Class, V]) -> V:
    return get_injected_instance(class_, context)
