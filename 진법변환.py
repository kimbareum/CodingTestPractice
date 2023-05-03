n = 9 # 10진법 자연수
t = 2 # 목표하는 진법

answer = ''

while n >= 1:
    rest = n % t
    n //= t
    answer = str(rest) + answer

print(answer)