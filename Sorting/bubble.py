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

def bubblesort(array, n=None):
    if n == None: 
        n = len(array) # if n not passed in set n to entirety
    for i in range(0, n): # from 0 to end of array

        if (SHOW_ITER):
            print(array)

        for j in range(n-1, i, -1): # from end of array to ith smallest
            if array[j] < array[j-1]: # bubble smallest element down
                array[j], array[j-1] = array[j-1], array[j] # swap
    return


def bubblesortV2(array, n=None):
    if n == None:
        n = len(array) # if n not passed in set n to entirety
    i = 0
    while True: # infinite loop from i = 0 onwards
        done = True # boolean to check if swaps have been made

        if (SHOW_ITER):
            print(array)

        for j in range(n-1, i, -1): # from end of array to ith smallest
            if array[j] < array[j-1]: # bubbles smallest element down
                array[j], array[j-1] = array[j-1], array[j] # swap
                done = False # swapped
        if done == True: # check if no swapping left
            return

def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # # Bubble Sort
    # print(f"Testing Bubble Sort")
    # test_sample = sample.copy()
    # bubblesort(test_sample)
    # print(f"Sorted: {test_sample}")

    # Bubble Sort V2
    print(f"Testing Buuble Sort V2")
    test_sample = sample.copy()
    bubblesortV2(test_sample)
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()