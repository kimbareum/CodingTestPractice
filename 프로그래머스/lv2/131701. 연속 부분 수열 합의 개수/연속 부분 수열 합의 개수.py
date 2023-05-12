def solution(elements):
    data = set()
    elements2 = elements[:] + elements[:]
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            data.add(sum(elements2[j:j+i]))
    return len(data)