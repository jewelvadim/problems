# Task - create infinity iterator

# Solution 1
from typing import Any, Iterable, Iterator


class CyclicIterator:
    _collection: Iterable
    _iterator: Iterator

    def __init__(self, collection: Iterable) -> None:
        self._collection = collection
        self._iterator = iter(self._collection)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        try:
            return next(self._iterator)
        except StopIteration:
            self._iterator = iter(self._collection)
            return next(self._iterator)
          



# Solution 2
from itertools import cycle
from typing import Any, Iterable, Iterator


class CyclicIterator:
    _iterator: Iterator

    def __init__(self, collection: Iterable) -> None:
        self._iterator = cycle(collection)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        return next(self._iterator)
