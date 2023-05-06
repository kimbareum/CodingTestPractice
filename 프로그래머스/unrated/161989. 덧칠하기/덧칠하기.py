from collections import deque 
def solution(n, m, section):
    if m == 1:
        return len(section)
    section = deque(section)
    answer = 0
    start = section.popleft()
    while section :
        now = section.popleft()
        if now >= start+m:
            answer += 1
            start = now
    return answer+1