def solution(arr1, arr2):
    answer = [[a+b for a,b in zip(c,d)] for c,d in zip(arr1,arr2)]
    return answer