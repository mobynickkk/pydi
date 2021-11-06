import typing as T
from queue import PriorityQueue


class PriorityUniqueQueue:
    __dict: dict
    __queue: PriorityQueue

    def __init__(self):
        self.__dict = dict()
        self.__queue = PriorityQueue()

    def put(self, value: T.Tuple[int, T.Any]):
        self.__dict[value[1]] = min(self.__dict.get(value[1], self.Inf()), value[0])
        self.__queue = PriorityQueue()
        self.__put_all(self.__dict.items())
        
    def __put_all(self, values: T.Iterable[T.Tuple[int, T.Any]]):
        for value in values:
            self.__queue.put((value[1], value[0]))

    def empty(self) -> bool:
        return self.__queue.empty()

    def get(self) -> T.Any:
        return self.__queue.get()[0]

    class Inf:

        def __gt__(self, other):
            return True

        def __lt__(self, other):
            return False
