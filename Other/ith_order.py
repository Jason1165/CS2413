import random
import copy

SHOW_ITER = True
MIN_SIZE = 5
MAX_SIZE = 10
MIN_NUM = 5
MAX_NUM = 20


def minimum(array, n=None):
    if (n == None):
        n = len(array)

    mini = array[0]
    for i in range(1, n):
        if (mini > array[i]):
            mini = array[i]
    return mini

def maximum(array, n=None):
    if (n == None):
        n = len(array)

    maxi = array[0]
    for i in range(1, n):
        if (maxi < array[i]):
            maxi = array[i]
    return maxi

def partition(array, start, end):
    x = array[end] # the pivot
    i = start-1 # highest index into the low side
    for j in range(start, end): # process each element other than the pivot
        if array[j] <= x: # does this element belong on the low side?
            i=i+1 # index of a new slot in the low side
            array[i], array[j] = array[j], array[i] # put this element there
    array[i+1], array[end] = array[end], array[i+1] # pivot goes just to the right of the low slide
    return i+1 # new index of the pivot

def randomized_partition(array, start, end):
    index = random.randint(start, end)
    x = array[index]
    array[index], array[end] = array[end], array[index]
    return partition(array, start, end)

def randomized_select(array, p, r, i):
    print(array[p:r+1])
    if (p == r):
        return array[p]
    q = randomized_partition(array, p, r)
    k = q - p + 1
    if (i == k):
        return array[q]
    elif (i < k):
        return randomized_select(array, p, q-1, i)
    return randomized_select(array, q+1, r, i-k)

def main():
    sample = [random.randint(MIN_NUM, MAX_NUM) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]

    print(f"Original Array: {sample}")

    # Radix Sort
    print(f"Testing Ith Order Statistics")
    test_sample = sample.copy()
    index = random.randint(1, len(test_sample))
    res = randomized_select(test_sample, 0, len(test_sample)-1, index)
    print(f"Looking for {index}th smallest: {res}")


if __name__ == "__main__":
    main()