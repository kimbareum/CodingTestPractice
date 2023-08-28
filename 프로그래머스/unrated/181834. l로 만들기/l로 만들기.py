import re

def solution(myString):
    return re.sub(r'[abcdefghijk]', 'l', myString)