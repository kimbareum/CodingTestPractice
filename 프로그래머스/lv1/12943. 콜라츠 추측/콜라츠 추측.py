def collatz(num, cnt):
    if num == 1:
        return cnt
    if cnt>=500:
        return -1
    if num%2 == 0:
        cnt = collatz(num//2,cnt+1)
    else :
        cnt = collatz(num*3+1,cnt+1)
    return cnt

def solution(num):
    if num==1: return 0
    cnt = 0
    cnt = collatz(num,cnt)
    return cnt