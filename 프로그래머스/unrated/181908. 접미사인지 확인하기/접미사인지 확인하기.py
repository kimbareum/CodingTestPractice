import re

def solution(my_string, is_suffix):
    return 1 if re.search(f'{is_suffix}$', my_string) else 0