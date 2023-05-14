from collections import deque

def solution(priorities, location):
    priority_map = deque(enumerate(priorities))
    answer = 1
    while True:
        top_index = priority_map.index(max(priority_map, key = lambda x: x[1]))
        priority_map.rotate(-top_index)
        if priority_map[0][0] == location:
            return answer
        else:
            priority_map.popleft()
            answer += 1
