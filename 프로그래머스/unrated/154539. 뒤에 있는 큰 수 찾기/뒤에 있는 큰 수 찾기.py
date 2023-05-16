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

# def solution(numbers):
#     stack = []
#     result = [-1] * len(numbers)
#     for i in range(len(numbers)):
#         while stack and numbers[stack[-1]] < numbers[i]:
#             result[stack.pop()] = numbers[i]

#         stack.append(i)

#     return result

# def solution(numbers):
#     q = [[int(1e6), -1]]
#     ans = [0]*(len(numbers))

#     for i, x in enumerate(numbers):
#         while q[-1][0] < x:
#             ans[q.pop()[1]] = x
#         q.append([x, i])

#     return [-1 if n == 0 else n for n in ans]