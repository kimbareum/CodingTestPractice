def solution(clothes):
    answer = 1
    equipment = {}
    for item, kind in clothes:
        if not equipment.get(kind):
            equipment.update({kind:[item]})
        else:
            equipment[kind].append(item)
            
    for items in equipment.values():
        answer *= len(items)+1   
    return answer-1

# from collections import Counter

# def solution(clothes):
#     answer = 1
#     count = Counter(map(lambda x: x[1], clothes))
#     for i in count.values():
#         answer *= i+1
#     return answer - 1
