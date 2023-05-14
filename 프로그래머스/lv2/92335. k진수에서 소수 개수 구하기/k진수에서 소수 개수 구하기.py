def solution(n, k):
    answer = 0
    #진법변환
    numbers = ''
    while n >= 1:
        rest = n % k
        n //= k
        numbers = str(rest) + numbers
        
    numbers = [int(i) for i in numbers.split('0') if i]
    
    # 소수 판별
    for number in numbers:
        if number <= 1:
            continue
        for i in range(2,int(number**0.5)+1):
            if number%i == 0:
                break
        else:answer += 1
        
    return answer