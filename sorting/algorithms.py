from typing import Union, List

NumberList = List[Union[int, float]]


def bubble_sort(arr: NumberList) -> NumberList:
    length = len(arr)
    for i in range(length):
        check = True
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j], arr[j + 1]
                check = False
        if check:
            break

    return arr


def quick_sort_rcu(arr: NumberList) -> NumberList:
    length = len(arr)
    if length == 1 or arr == []:
        return arr

    pv = arr[-1]
    i = 0
    j = -1
    while i < length:
        if arr[i] <= pv:
            j += 1
        if i != j and arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1

    a = quick_sort_rcu(arr[:j]) if j > 0 else []
    c = quick_sort_rcu(arr[j + 1:]) if j + 1 < length else []
    return a + arr[j:j + 1] + c


def merge_sort(arr: NumberList) -> NumberList:
    length = len(arr)

    if length == 1:
        return arr

    mid = length // 2

    head, ass = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    lh, la = len(head), len(ass)
    new = []
    i, j = 0, 0
    while i < lh:
        while j < la:
            if head[i] <= ass[j]:
                new.append(head[i])
                i += 1
                break
            else:
                new.append(ass[j])
                j += 1
        else:
            break
    if i == lh or j == la:
        new += head[i:] + ass[j:]

    return new
