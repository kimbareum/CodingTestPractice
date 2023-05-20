def solution(topping):
    left = []
    right = []
    answer = 0
    temp = set()
    for i in topping:
        temp.add(i)
        left.append(len(temp))
    temp = set()
    for j in topping[::-1]:
        temp.add(j)
        right.append(len(temp))
    for l, r in zip(left,right[len(right)-2::-1]):
        if l == r:
            answer += 1
    return answer

# from collections import Counter

# def solution(topping):
#     answer = 0
#     dic = Counter(topping)
#     set_dic = set()
#     answer = 0

#     for i in topping:
#         dic[i] -= 1
#         set_dic.add(i)
#         if dic[i] == 0:
#             dic.pop(i)
#         if len(dic) == len(set_dic):
#             answer += 1

#     return answer