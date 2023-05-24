def solution(n, k):
    answer = []
    num_list = list(range(1,n+1))
    facto = 1
    for i in num_list:
        facto *= i
    for i in range(n, 0, -1):
        facto //= i
        q, k = k//facto, k%facto
        if k == 0:
            answer.append(num_list.pop(q-1))
            answer += num_list[::-1]
            break
        answer.append(num_list.pop(q))
    return answer