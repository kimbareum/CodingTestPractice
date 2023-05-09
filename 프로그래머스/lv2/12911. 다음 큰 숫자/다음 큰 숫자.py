def solution(n):
    a = n
    while True:
        a += 1
        if bin(n).count('1') == bin(a).count('1'):
            return a