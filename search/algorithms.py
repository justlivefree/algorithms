import math
from typing import Any, Union

IndexSupportType = Union[list, tuple, str, bytearray, bytes]
NumberArray = Union[list[int | float], tuple[int | float]]


def liner_search(arr: IndexSupportType, data: Any) -> int | None:
    for i in range(len(arr)):
        if arr[i] == data:
            return i


def binary_search(arr: IndexSupportType, data: Union[int, float]) -> int | None:
    length = len(arr)
    i, j = 0, length
    while abs(i - j) != 1:
        mid = (i + j) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] > data:
            j = mid
        else:
            i = mid


def jump_search(arr: IndexSupportType, data: Union[int, float]) -> int | None:
    length = len(arr)
    block = int(math.sqrt(length))
    for i in range(0, length, block):
        if arr[i] >= data:
            return liner_search(arr[i - block: i + 1], data)
