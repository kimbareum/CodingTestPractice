from collections import deque
def solution(ingredient):
    if len(ingredient) < 4:
        return 0
    ing = deque(ingredient)
    answer = 0
    queue = [ing.popleft() for _ in range(3)]
    while ing:
        queue.append(ing.popleft())
        while len(queue) >=4 and queue[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                queue.pop()
    return answer