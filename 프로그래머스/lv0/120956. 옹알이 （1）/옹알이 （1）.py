from itertools import permutations

def solution(babbling):
    babbles = ["aya", "ye", "woo", "ma"]
    babble_list = babbles[:]
    answer = 0
    
    for i in range(2,len(babbles)+1):
        babble_list += [''.join(permutation) for permutation in permutations(babbles,i)]
        
    for i in babbling:
        if i in babble_list:
            answer += 1
        
    return answer