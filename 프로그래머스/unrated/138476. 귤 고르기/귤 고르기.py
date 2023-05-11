from collections import Counter

def solution(k, tangerine):
    count = sorted(Counter(tangerine).values(), reverse=True)
    for i, size in enumerate(count,1):
        k -= size
        if k <= 0:
            return i   