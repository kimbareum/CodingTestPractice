def solution(n):
    divisor = []
    for i in range(1,n//2+1): #약수중 가장 큰 경우는 2로 나눈 경우이기때문에 1에서 n//2+1 까지만 고려
        if n%i == 0:
            divisor.append(i)
    return sum(divisor)+n