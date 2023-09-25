def solution(arr, n):
    flag = len(arr)%2
    return [arr[i] + n if not i%2 else arr[i] for i in range(len(arr))] if flag else [arr[i] + n if i%2 else arr[i] for i in range(len(arr))]