def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            prev, _ = stack.pop()
            answer[prev] = i - prev    
        stack.append((i, prices[i]))
    else:
        for i, j in stack:
            answer[i] = len(prices) -1 - i
    return answer