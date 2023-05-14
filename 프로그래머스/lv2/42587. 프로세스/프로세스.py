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

# index(max) 를 매번 넣는게 생각보다 느릴지도.

# def solution(priorities, location):
#     answer = 0
#     priorities = deque(priorities)
#     top_priority = max(priorities)
#     while True:
#         curr = priorities.popleft()
#         if top_priority == curr:
#             answer += 1
#             if location == 0:
#                 break
#             else:
#                 location -= 1
#             top_priority = max(priorities)
#         else:
#             priorities.append(curr)
#             if location == 0:
#                 location = len(priorities)-1
#             else:
#                 location -= 1
#     return answer