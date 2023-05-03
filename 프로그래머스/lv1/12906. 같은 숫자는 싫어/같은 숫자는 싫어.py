from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    while arr:
        num = arr.popleft()
        if answer[-1] != num:
            answer.append(num)
    return answer