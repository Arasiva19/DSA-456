import random
import time

def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1  # comparison
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3  # swap
    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps += 1  # comparison
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            steps += 3  # swap
    return steps

def insertion_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        steps += 1  # initial comparison for while
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 3  # shift counted as 3 operations
        my_list[j + 1] = key
        steps += 1  # placement
    return steps

def quick_sort(my_list):
    steps = [0]
    def _quick_sort(lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst)//2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        steps[0] += len(lst)  # count partition scanning
        return _quick_sort(left) + middle + _quick_sort(right)
    sorted_list = _quick_sort(my_list)
    my_list[:] = sorted_list
    return steps[0]

def insertion_sort_range(my_list, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        steps += 1
        while j >= left and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 3
        my_list[j + 1] = key
        steps += 1
    return steps

def generate_worst_case(n):
    return list(range(n, 0, -1))

def generate_best_case(n):
    return list(range(n))

def generate_average_case(n):
    return [random.randint(0, n) for _ in range(n)]

if __name__ == "__main__":
    # Test sorting list of length 100
    base = [random.randint(0, 1000) for _ in range(100)]
    for f in [bubble_sort, selection_sort, insertion_sort, quick_sort]:
        arr = base.copy()
        steps = f(arr)
        print(f"{f.__name__}: sorted? {arr == sorted(base)} | steps = {steps}")
