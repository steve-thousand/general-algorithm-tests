import random
import time
import sys
from enum import Enum

class Case(Enum):
    BEST = 1
    WORST = 2
    AVERAGE = 3

def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr)):
            # n
            if i + 1 < len(arr) and arr[i] > arr[i + 1]:
                scratch = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = scratch
                sorted = False
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)):
        # n
        min_index = i
        for j in range(i + 1, len(arr)):
            # n
            if arr[j] < arr[min_index]:
                min_index = j
        scratch = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = scratch
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # n
        index = i
        while index > 0 and arr[index - 1] > arr[index]:
            # worst case n, best case 1
            scratch = arr[index]
            arr[index] = arr[index - 1]
            arr[index - 1] = scratch
            index -= 1
    return arr

TOTAL_RUNS = 10

def verify(algorithm, name):

    # first let's test that it actually sorts correctly
    arr = list(range(1, 20))
    random.shuffle(arr)
    arr = algorithm(arr)
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise Exception("NOT SORTED!")

    print("timing " + name + " sort...")

    def time_the_algorithm(algorithm, case):
        total = 0
        min = sys.maxsize
        max = 0

        sizes = [1000,5000,10000]

        for size in sizes:
            for i in range(0, TOTAL_RUNS):

                arr = list(range(1, size))
                if case == Case.WORST:
                    # for worst case, reverse entire array
                    arr = list(reversed(arr))
                elif case == Case.AVERAGE:
                    # average case, random order
                    random.shuffle(arr)

                start = time.time()
                arr = algorithm(arr)
                end = time.time()

                elapsed = end - start
                total += elapsed
                if elapsed > max:
                    max = elapsed
                if elapsed <= min:
                    min = elapsed

            print(name + ", n={0:} - ".format(size) + str(case) + ": avg {0:.2f}s, min {1:.2f}s, max {2:.2f}s".format(total/TOTAL_RUNS, min, max))

    # worst case
    time_the_algorithm(algorithm, Case.WORST)
    # avg case
    time_the_algorithm(algorithm, Case.AVERAGE)
    # best case
    time_the_algorithm(algorithm, Case.BEST)
    

verify(insertion_sort, "insertion")
verify(selection_sort, "selection")
verify(bubble_sort, "bubble")