import random
import time
import sys

def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr)):
            if i + 1 < len(arr) and arr[i] > arr[i + 1]:
                scratch = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = scratch
                sorted = False
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        scratch = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = scratch
    return arr

def insertion_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                scratch = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = scratch
            else:
                break
    return arr

TOTAL_RUNS = 10

def verify(algorithm, name):

    # first let's test that it actually sorts correctly
    arr = range(1, 20)
    random.shuffle(arr)
    arr = algorithm(arr)
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise Exception("NOT SORTED!")

    # now let's time it
    total = 0
    min = sys.maxint
    max = 0
    for i in range(0, TOTAL_RUNS):
        arr = range(1, 2000)
        random.shuffle(arr)

        start = time.time()
        arr = algorithm(arr)
        end = time.time()

        elapsed = end - start
        total += elapsed
        if elapsed > max:
            max = elapsed
        if elapsed < min:
            min = elapsed

    print(name + " : avg {0:.2f}s, min {0:.2f}s, max {0:.2f}s".format(total/TOTAL_RUNS, min, max))

verify(insertion_sort, "insertion")
verify(selection_sort, "selection")
verify(bubble_sort, "bubble")