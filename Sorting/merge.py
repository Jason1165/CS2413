import random
import copy
import sys

SHOW_ITER = True
MIN_SIZE = 16
MAX_SIZE = 16
MIN_NUM = -100
MAX_NUM = 100

if len(sys.argv) > 1:
    MIN_SIZE = int(sys.argv[1])
    MAX_SIZE = int(sys.argv[2])
    MIN_NUM = int(sys.argv[3])
    MAX_NUM = int(sys.argv[4])

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
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # Merge Sort
    print(f"Testing Merge Sort")
    test_sample = sample.copy()
    mergesort(test_sample)
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()
