
# 2026-05-27 18:01:54.852585
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# 2026-05-27 20:34:02.879987
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

