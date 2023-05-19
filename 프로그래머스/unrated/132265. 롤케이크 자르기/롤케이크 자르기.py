def solution(topping):
    left = []
    right = []
    answer = 0
    temp = set()
    for i in topping:
        temp.add(i)
        left.append(len(temp))
    temp = set()
    for j in topping[::-1]:
        temp.add(j)
        right.append(len(temp))
    for l, r in zip(left,right[len(right)-2::-1]):
        if l == r:
            answer += 1
    return answer