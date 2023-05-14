import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K :
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one+two*2)
        answer += 1
        if len(scoville) <= 1:
            break
    return -1 if len(scoville) <= 1 and scoville[0] < K else answer