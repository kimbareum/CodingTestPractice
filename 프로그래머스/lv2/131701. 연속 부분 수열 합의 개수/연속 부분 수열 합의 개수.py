# def solution(elements):
#     data = set()
#     elements2 = elements[:] + elements[:]
#     for i in range(1, len(elements) + 1):
#         for j in range(len(elements)):
#             data.add(sum(elements2[j:j+i]))
#     return len(data)

def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):             # 처음꺼부터 마지막꺼까지 1개씩 순회
        ssum = elements[i]          # 길이가 1인 경우를 추가
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]  # 2인경우부터 하나씩 추가
            res.add(ssum)
    return len(res)
