from collections import deque
def solution(order):
    answer = 0
    main = deque([i for i in range(1, len(order)+1)])
    order = deque(order)
    stack = []
    while order:
        while main and main[0] <= order[0]:
            stack.append(main.popleft())
        while stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
        if stack and stack[-1] > order[0] :
            break
    return answer
