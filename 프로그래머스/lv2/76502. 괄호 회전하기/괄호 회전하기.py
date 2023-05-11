# from collections import deque

# def solution(s):
#     dic = dict(zip(('[',']','{','}','(',')'),(1,-1,2,-2,3,-3)))
#     s = deque(s)
#     answer = 0
#     for _ in range(len(s)):
#         q1 = deque(s)
#         q2 = []
#         while q1:
#             q2.append(q1.popleft())
#             while len(q2) > 1 and dic.get(q2[-1]) < 0 and dic.get(q2[-1])+dic.get(q2[-2]) == 0:
#                 q2.pop()
#                 q2.pop()
#         if q2 == []:
#             answer += 1   
#         s.rotate(-1)
#     return answer


from collections import deque

def check(s):
    while True:
        if "()" in s: s=s.replace("()","")
        elif "{}" in s: s=s.replace("{}","")
        elif "[]" in s: s=s.replace("[]","")
        else: return False if s else True       

def solution(s):
    ans = 0
    que = deque(s)

    for i in range(len(s)):
        if check(''.join(que)): ans+=1
        que.rotate(-1)
    return ans
