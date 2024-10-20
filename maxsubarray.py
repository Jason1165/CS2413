import random

def bruteforce(array):
    maxsum = 0
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            sum = 0
            for k in range(i, j+1):
                sum += array[k]
            if sum > maxsum:
                maxsum = sum
    return maxsum

def modified_bruteforce(array):
    maxsum = 0
    for i in range(0, len(array)):
        sumcurrent = 0
        for j in range(i, len(array)):
            sumcurrent += array[j]
            if sumcurrent > maxsum:
                maxsum = sumcurrent
    return maxsum

def maxPrefix(array, start, end):
    maxi = 0
    prefixsum = 0
    for i in range(start, end+1):
        prefixsum += array[i]
        if prefixsum > maxi:
            maxi = prefixsum
    return maxi

def maxSuffix(array, start, end):
    maxi = 0
    suffixsum = 0
    for i in range(end, start-1, -1):
        suffixsum += array[i]
        if suffixsum > maxi:
            maxi = suffixsum
    return maxi

def maxSum(array, start, end):
    print(f"Looking at: {array[start:end+1]}")
    if start > end:
        return 0
    if start == end:
        if array[start] < 0:
            return 0
        return array[start]
    mid = (start+end)//2
    LMax = maxSum(array, start, mid) # recursively find max sum of subarray on left half
    RMax = maxSum(array, mid+1, end) # recursively find max sum of subarray on right half
    SuffLMax = maxSuffix(array, start, mid) # find max sum of suffix on left O(n)
    PrefRMax = maxPrefix(array, mid+1, end) # find max sum of prefix on right O(n)
    res = max(LMax, RMax, (SuffLMax + PrefRMax)) # O(1)
    print(f"start: {start}, end: {end}, LMax: {LMax}, RMax: {RMax}, SuffL: {SuffLMax}, PrefR: {PrefRMax}, Maximum is currently: {res}")
    return res

def main():
    sample = [random.randint(-10, 10) for _ in range(16)]
    print(f"Array: {sample}")
    print(f"Bruteforce: {bruteforce(sample)}")
    print(f"Modified Bruteforce: {modified_bruteforce(sample)}")
    print(f"Divide and Conquer: {maxSum(sample, 0, len(sample)-1)}")

if __name__ == "__main__":
    main()