import random
import time
import copy

SHOW_ITER = True
SHOW_TIME = False
MIN_SIZE = 5
MAX_SIZE = 30
SIZE = 16
MIN_NUM = -100
MAX_NUM = 100

def mergesort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if start >= end - 1:
        return

    if (SHOW_ITER):
        print(f"Merge Sort: {array[start:end]}")

    mid = (start + end) // 2
    mergesort(array, start, mid)  # Sort first half
    mergesort(array, mid, end)    # Sort second half
    merge(array, start, mid, end) # Merge both halves

def merge(array, start, mid, end):
    # create temp arrays
    left = array[start:mid]
    right = array[mid:end]

    # pointers
    p1 = p2 = 0
    k = start

    # merge two arrays back
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            array[k] = left[p1]
            p1 += 1
        else:
            array[k] = right[p2]
            p2 += 1
        k += 1

    # copy remaining elements of left[]
    while p1 < len(left):
        array[k] = left[p1]
        p1 += 1
        k += 1
    
    # copy remaining elements of right[]
    while p2 < len(right):
        array[k] = right[p2]
        p2 += 1
        k += 1

    if (SHOW_ITER):
        print(f"Merging   : {array[start:end]}")
    

def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]

    print(f"Original Array: {sample}")

    # Merge Sort
    print(f"Testing Merge Sort")
    test_sample = sample.copy()
    start_time = time.time()
    mergesort(test_sample)
    end_time = time.time()
    print(f"Sorted: {test_sample}")
    if (SHOW_TIME):
        print(f"Elapsed Time: {end_time - start_time}")

if __name__ == "__main__":
    main()
