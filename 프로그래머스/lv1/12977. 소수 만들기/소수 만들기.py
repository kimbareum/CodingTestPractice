from itertools import combinations

def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    nums2 = [sum(i) for i in combinations(nums,3)]
    for i in nums2:
        if isprime(i):
            answer += 1
    return answer