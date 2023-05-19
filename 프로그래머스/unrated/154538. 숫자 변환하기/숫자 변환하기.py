from collections import deque

def solution(x, y, n):    
    if x==y:
        return 0
    queue = deque([(x,0)])
    answer = [0 for _ in range(y+1)]
    while queue:
        curr, count = queue.popleft()
        count += 1
        if curr+n <= y and answer[curr+n] == 0:
            answer[curr+n] = count
            queue.append((curr+n, answer[curr+n]))
        if curr*2 <= y:
            if answer[curr*2] == 0:
                answer[curr*2] = count
                queue.append((curr*2, answer[curr*2]))
            else:
                if answer[curr*2] > count:
                    answer[curr*2] = count
                    queue.append((curr*2, answer[curr*2]))
        if curr*3 <= y:
            if answer[curr*3] == 0:
                answer[curr*3] = count
                queue.append((curr*3, answer[curr*3]))
            else:
                if answer[curr*3] > count:
                    answer[curr*3] = min(count,answer[curr*3])
                    queue.append((curr*3, answer[curr*3]))
    return answer[-1] if answer[-1] else -1
