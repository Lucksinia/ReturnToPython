import random
import timeit
from functools import partial


def bubble_sort(lst: list) -> list:
    """Sorting arrays by bauble sort with premature optimization

    :param list lst: unsorted array
    :return list: sorted array
    """
    for i in range(len(lst)):
        already = True
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                already = False
        if already:  # if there was no sorting in previous cycle, we are done!
            break
    return lst


def selection_sort(lst: list) -> list:
    """Sorting arrays by selection

    :param list lst: unsorted array
    :return list: sorted array
    """
    for i in range(len(lst)):
        step = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[step]:
                step = j
        lst[i], lst[step] = lst[step], lst[i]
    return lst


def insertion_sort(lst: list) -> list:
    """Sorting arrays by insertion

    :param list lst: unsorted array
    :return list: sorted array
    """
    for i in range(1, len(lst)):
        item = lst[i]
        j = i - 1
        while j >= 0 and item < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item
    return lst


def merge(left: list, right: list) -> list:
    """merging arrays with premature optimization

    :param list left: left half of unsorted array
    :param list right: right half of assorted array
    :return list: sorted array
    """
    # premature optimization
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    result = []
    ileft = iright = 0
    while len(result) < len(left) + len(right):
        if left[ileft] <= right[iright]:
            result.append(left[ileft])
            ileft += 1
        else:
            result.append(right[iright])
            iright += 1
        # another premature optimization
        if iright == len(right):
            result += left[ileft:]
            break
        elif ileft == len(left):
            result += right[iright:]
    return result


def merge_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    middle = len(lst) // 2
    return merge(left=merge_sort(lst[:middle]), right=merge_sort(lst[middle:]))


def quicksort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    low, same, high = [], [], []
    pivot = lst[random.randint(0, len(lst) - 1)]
    for item in lst:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


unsorted_lst = [random.randint(0, 1000) for i in range(10000)]

# !still Not DRY enough!
timing = partial(timeit.timeit, globals=globals(), number=10)

bauble_result = timing("bubble_sort(unsorted_lst)")
selection_result = timing("selection_sort(unsorted_lst)")
insertion_result = timing("insertion_sort(unsorted_lst)")
merge_result = timing("merge_sort(unsorted_lst)")
quicksort_result = timing("quicksort(unsorted_lst)")
print(f"optimized bubble: {bauble_result:.03} s")
print(f"selection: {selection_result:.03} s")
print(f"insertion: {insertion_result:.03} s")
print(f"merge: {merge_result:.03} s")
print(f"quicksort: {quicksort_result:.03} s")
