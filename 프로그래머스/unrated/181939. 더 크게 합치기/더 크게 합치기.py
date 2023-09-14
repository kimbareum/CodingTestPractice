def solution(a, b):
    one = int(str(a) + str(b))
    two = int(str(b) + str(a))
    return one if one >= two else two