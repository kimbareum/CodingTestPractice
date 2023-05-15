def solution(land):
    for n in range(len(land)-1,0,-1):
        for j in range(4):
            land[n-1][j] += max(land[n][i] for i in range(4) if i != j)
    return max(land[0])