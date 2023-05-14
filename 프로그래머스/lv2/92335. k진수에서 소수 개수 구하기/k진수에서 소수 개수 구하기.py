def isprime(num):
    if num <= 1:
        return 0
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    numbers = ''
    while n >= 1:
        rest = n % k
        n //= k
        numbers = str(rest) + numbers
    numbers = [int(i) for i in numbers.split('0') if i]
    for number in numbers:
        answer += isprime(number)
    return answer