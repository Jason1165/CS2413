import random
import copy
import sys

SHOW_ITER = True
MIN_SIZE = 5
MAX_SIZE = 20
MIN_NUM = -100
MAX_NUM = 100

if len(sys.argv) > 1:
    MIN_SIZE = int(sys.argv[1])
    MAX_SIZE = int(sys.argv[2])
    MIN_NUM = int(sys.argv[3])
    MAX_NUM = int(sys.argv[4])

def insertionsort(array, n):
    for i in range(1, n): # from 1st element to end as nothing to compared 0th element with

        if (SHOW_ITER):
            print(array)
        
        key = array[i] # store value in key
        j = i - 1 # compare with everything before
        while j > -1 and array[j] > key: # swap down to proper position
            array[j+1] = array[j] # not right position so set it equal to the prev value
            j = j - 1 # decrement
        array[j+1] = key # found the right position

    if (SHOW_ITER):
        print(array)

def main():
    sample = [random.randint(-100, 100) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]
    
    print(f"Original Array: {sample}")

    # Insertion Sort
    print(f"Testing Insertion Sort")
    test_sample = sample.copy()
    insertionsort(test_sample, len(test_sample))
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()
    