def solution(s):
    s = sorted(map(int,s.split()))
    return f'{min(s)} {max(s)}'