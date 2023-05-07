def solution(ingredient):
    if len(ingredient) < 4:
        return 0
    answer = 0
    queue = []
    for i in ingredient:
        queue.append(i)
        while len(queue) >=4 and queue[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                queue.pop()
    return answer