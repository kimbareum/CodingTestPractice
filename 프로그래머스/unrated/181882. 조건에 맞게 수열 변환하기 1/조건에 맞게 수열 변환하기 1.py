def selector(num):
    if num>=50 and num%2 == 0 :
        return num/2
    elif num<50 and num%2 :
        return num*2
    return num

def solution(arr):
    return list(map(selector, arr))