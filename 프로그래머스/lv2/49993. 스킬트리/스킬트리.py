import re
def solution(skill, skill_trees):
    answer = 0
    for i, tree in enumerate(skill_trees):
        tree =  re.sub(f'[^{skill}]','',tree)
        
        is_true = True
        for i, char in enumerate(tree):
            if char != skill[i]:
                is_true = False
                break
        if is_true:
            answer += 1
    return answer