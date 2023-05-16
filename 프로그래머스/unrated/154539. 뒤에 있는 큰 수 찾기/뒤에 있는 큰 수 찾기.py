def solution(numbers):
    wait = []
    answer = []
    for i in numbers[::-1]:
        while wait:
            if wait[-1] > i:
                answer.append(wait[-1])
                wait.append(i)
                break
            else:
                wait.pop()
        if not wait:
            wait.append(i)
            answer.append(-1)
    return answer[::-1]