# from itertools import permutations

# def solution(numbers):
#     cases = []
#     for i in range(1, len(numbers)+1):
#         cases.extend(permutations(numbers,i)) 
#     cases = set([int(''.join(i)) for i in cases])
#     answer = 0
#     for num in cases:
#         if num < 2:
#             continue
#         for i in range(2,int(num**0.5)+1):
#             if num%i == 0:
#                 break
#         else:
#             answer += 1 
#     return answer

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        if not a:
            break
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)