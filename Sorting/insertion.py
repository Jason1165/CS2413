import random
import time
import copy

SHOW_ITER = True
SHOW_TIME = False
MIN_SIZE = 5
MAX_SIZE = 30
MIN_NUM = -100
MAX_NUM = 100

def insertionsort(array, n=None):
    if n == None:
        n = len(array) # if n not passed in set n to entirety
    for i in range(1, n): # from 1st element to end as nothing to compared 0th element with

        if (SHOW_ITER):
            print(array)
        
        key = array[i] # store value in key
        j = i - 1 # compare with everything before
        while j > -1 and array[j] > key: # swap down to proper position
            array[j+1] = array[j] # not right position so set it equal to the prev value
            j = j - 1 # decrement
        array[j+1] = key # found the right position
    return

def main():
    sample = [random.randint(-100, 100) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]
    
    print(f"Original Array: {sample}")

    # Insertion Sort
    print(f"Testing Insertion Sort")
    test_sample = sample.copy()
    start_time = time.time()
    insertionsort(test_sample)
    end_time = time.time()
    print(f"Sorted: {test_sample}")
    if (SHOW_TIME):
        print(f"Elapsed Time: {end_time - start_time}")

if __name__ == "__main__":
    main()
    