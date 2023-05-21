from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    max_count = len(queue1)*4
    while sum1 != sum2:
        if not queue1 or not queue2 or answer >= max_count:
            return -1
            break
        if sum1 > sum2:
            sum2 += queue1[0]
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
        else:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        answer += 1
    return answer