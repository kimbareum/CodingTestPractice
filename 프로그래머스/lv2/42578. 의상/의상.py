def solution(clothes):
    answer = 1
    equipment = {}
    
    for i, j in clothes:
        if not equipment.get(j):
            equipment.update({j:[i]})
        else:
            equipment[j].append(i)
            
    for items in equipment.values():
        answer *= len(items)+1   
    return answer-1