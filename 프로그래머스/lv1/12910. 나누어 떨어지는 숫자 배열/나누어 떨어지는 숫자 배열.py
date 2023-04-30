def solution(arr, divisor):
    answer = sorted([n for n in arr if n%divisor == 0])
    return answer if len(answer)!=0 else [-1]