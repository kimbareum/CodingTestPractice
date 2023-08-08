def solution(data, col, row_begin, row_end):
    data = sorted(data, key=(lambda x:(x[col-1], -x[0])))
    s = 0
    for i in range(row_begin-1, row_end):
        temp = 0
        for j in data[i]:
            temp += j%(i+1)
        s = s^temp
    return s