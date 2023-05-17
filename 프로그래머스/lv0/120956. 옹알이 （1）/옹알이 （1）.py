import re

def solution(babbling):
    babble = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        babbling[i] = re.sub('(aya|ye|woo|ma)', ' ',babbling[i]).strip()
    
    return len([i for i in babbling if not i])