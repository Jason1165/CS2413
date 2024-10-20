import random
import copy
import sys

SHOW_ITER = True
MIN_SIZE = 5
MAX_SIZE = 30
MIN_NUM = -100
MAX_NUM = 100

if len(sys.argv) > 1:
    MIN_SIZE = int(sys.argv[1])
    MAX_SIZE = int(sys.argv[2])
    MIN_NUM = int(sys.argv[3])
    MAX_NUM = int(sys.argv[4])

# inclusive end
def quicksort(array, start=0, end=None):
    if (end == None):
        end = len(array)-1
    if (start < end):
        if (SHOW_ITER):
            print(f"After Quick Sort:\n\t{array[start:end+1]}")
        q = partition(array, start, end) # partition the subarray around the pivot, which ends in A[q]
        quicksort(array, start, q-1) # recursively sort the low side
        quicksort(array, q+1, end) # recursively sort the high side

# inclusive start and end
def partition(array, start, end):
    x = array[end] # the pivot
    i = start-1 # highest index into the low side
    for j in range(start, end): # process each element other than the pivot
        if array[j] <= x: # does this element belong on the low side?
            i=i+1 # index of a new slot in the low side
            array[i], array[j] = array[j], array[i] # put this element there
    array[i+1], array[end] = array[end], array[i+1] # pivot goes just to the right of the low slide
    if (SHOW_ITER):
        print(f"Partitioned around {x}:\n\t{array[start:end+1]}") 
    return i+1 # new index of the pivot

def randomized_quicksort(array, start=0, end=None):
    if (end == None):
        end = len(array)-1
    if (start < end):
        if (SHOW_ITER):
            print(f"After Randomized Quick Sort:\n\t{array[start:end+1]}")
        q = randomized_partition(array, start, end)
        randomized_quicksort(array, start, q-1)
        randomized_quicksort(array, q+1, end)

def randomized_partition(array, start, end):
    index = random.randint(start, end)
    x = array[index]
    array[index], array[end] = array[end], array[index]
    return partition(array, start, end)

def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # Quick Sort
    print(f"Testing Quick Sort")
    test_sample = sample.copy()
    quicksort(test_sample)
    print(f"Sorted: {test_sample}")

    # Randomized Quick Sort
    print(f"\nTesting Randomized Quick Sort")
    test_sample = sample.copy()
    randomized_quicksort(test_sample)
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()
