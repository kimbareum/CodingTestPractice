def solution(n):
    answer = [i for i in range(n+1)]
    for i in answer[2:]:
        if i > 0:
            j = 2
            while i * j <= n:
                answer[i*j] = 0
                j+=1
    return len(answer[2:])-answer[2:].count(0)
        
