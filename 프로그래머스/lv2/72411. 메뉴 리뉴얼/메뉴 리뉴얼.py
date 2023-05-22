from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    cases = []
    for i in course:
        temp = []
        for order in orders:
            temp.extend([list(case) for case in combinations(order,i)])
        cases.append(temp)
    
    for case in cases:
        count = Counter([''.join(sorted(i)) for i in case])
        if count:
            max_value = max(count.values())
            if max_value >= 2:
                answer.extend(filter(lambda x: count.get(x) == max_value, count))                   
    return sorted(answer)