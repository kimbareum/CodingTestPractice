def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        t = 1
        big, small = max(arr[i+1], arr[i]), min(arr[i+1], arr[i])
        while t > 0:
            t = big % small
            big, small = small, t
        arr[i+1] = arr[i] * arr[i+1] // big
    return arr[-1]