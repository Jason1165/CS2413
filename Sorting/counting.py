import random
import copy
import sys

SHOW_ITER = True
MIN_SIZE = 5
MAX_SIZE = 20
MIN_NUM = 0
MAX_NUM = 10

if len(sys.argv) > 1:
    MIN_SIZE = int(sys.argv[1])
    MAX_SIZE = int(sys.argv[2])
    MIN_NUM = int(sys.argv[3])
    MAX_NUM = int(sys.argv[4])

# end is exclusive
def countingsort(array, end, k):
    counts = [0]*(k+1)
    output = [-1]*end
    
    for j in range(0, end):
        counts[array[j]] = counts[array[j]] + 1
    # counts[i] now contains the number of elements equal to i

    for i in range(1,k+1):
        counts[i] = counts[i] + counts[i-1]
    # counts[i] now contains the number of elements less than or equal to i
    # copy array to output, starting from the end of array
    for j in range(end-1, -1, -1):
        if (SHOW_ITER):
            print(f"{output}")
        output[counts[array[j]] - 1] = array[j]
        counts[array[j]] = counts[array[j]] - 1
    
    return output

def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # Quick Sort
    print(f"Testing Counting Sort")
    test_sample = sample.copy()
    test_sample = countingsort(test_sample, len(test_sample), max(test_sample))
    print(f"Sorted: {test_sample}")

if __name__ == "__main__":
    main()
