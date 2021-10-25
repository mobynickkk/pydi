import typing as T

from .types import Class


class PriorityUniqueQueue:
    values: T.List[T.Any]
    queue: T.List[T.Tuple[Class, T.Any]]

    def __init__(self):
        self.values = list()
        self.queue = list()

    def put(self, value: T.Tuple[int, T.Any]):
        if value[1] in self.values:
            return
        self.values.append(value[1])
        self.queue.append(value)
        self.queue.sort(key=lambda x: x[0])

    def empty(self):
        return len(self.queue) == 0

    def get(self):
        return self.queue.pop(0)
