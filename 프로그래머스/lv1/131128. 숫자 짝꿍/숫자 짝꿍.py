from collections import Counter

def solution(X, Y):
    Z = set(X)&set(Y)
    if not Z:
        return "-1"
    X = Counter(X)
    Y = Counter(Y)
    A = [i*min(X[i],Y[i]) for i in Z]
    A = sorted(A,reverse=True)
    if A[0][0] == '0':
        return "0"
    return (''.join(A))