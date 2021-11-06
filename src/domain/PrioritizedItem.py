import typing as T
from dataclasses import dataclass, field


@dataclass(init=True, order=True)
class PrioritizedItem:
    priority: int
    item: T.Any = field(compare=False)
