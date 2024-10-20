import random
import copy
import sys

SHOW_ITER = True
MIN_SIZE = 5
MAX_SIZE = 15
MIN_NUM = 1000
MAX_NUM = 9999

if len(sys.argv) > 1:
    MIN_SIZE = int(sys.argv[1])
    MAX_SIZE = int(sys.argv[2])
    MIN_NUM = int(sys.argv[3])
    MAX_NUM = int(sys.argv[4])

def counting_sort_radix(array, n, exp):
    output = [0] * n
    counts = [0] * 10

    for i in range(n):
        index = (array[i] // exp) % 10
        counts[index] = counts[index] + 1
    
    for i in range(1, 10):
        counts[i] = counts[i] + counts[i-1]

    for i in range(n-1, -1, -1):
        index = (array[i] // exp) % 10
        output[counts[index]-1] = array[i]
        counts[index] -= 1
    
    for i in range(n):
        array[i] = output[i]

def radixsort(array, end, d):
    exp = 1 # place value
    for i in range(d):

        if (SHOW_ITER):
            print(f"After {i} column: {array}")

        counting_sort_radix(array, end, exp)
        exp *= 10

    if (SHOW_ITER):
        print(f"After {d} column: {array}")


def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # Radix Sort
    print(f"Testing Radix Sort")
    test_sample = sample.copy()
    radixsort(test_sample, len(test_sample), len(str(max(test_sample))))
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()