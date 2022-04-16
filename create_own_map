from typing import Callable, Iterable


# Task - create own map function
def my_map(func: Callable, iterable_object: Iterable) -> list:
    """Apply func to each element of the iterable object."""
    result = []
    iterator = iter(iterable_object)

    while True:
        try:
            item = next(iterator)

        except StopIteration:
            break

        else:
            result.append(func(item))

    return result


# Tests:
assert my_map(str, [1, 2, 3]) == ['1', '2', '3']
assert my_map(str, (1, 2, 3)) == ['1', '2', '3']
assert my_map(str, {1, 2, 3}) == ['1', '2', '3']
assert my_map(str, range(1, 4)) == ['1', '2', '3']
assert my_map(str, '123') == ['1', '2', '3']
assert my_map(str, []) == []
assert my_map(str, {1: 1, 2: 2, 3: 3}.keys()) == ['1', '2', '3']
assert my_map(str, {1: 1, 2: 2, 3: 3}.values()) == ['1', '2', '3']
assert my_map(str, (i for i in '123')) == ['1', '2', '3']
