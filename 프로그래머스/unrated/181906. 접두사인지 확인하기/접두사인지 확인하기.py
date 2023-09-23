import re

def solution(my_string, is_prefix):
    pattern = re.compile(f'^{is_prefix}')
    return 1 if pattern.match(my_string) else 0