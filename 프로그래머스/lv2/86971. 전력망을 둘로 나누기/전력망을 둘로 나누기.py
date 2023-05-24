def find(x,uf):
    if uf[x] != x:
        uf[x] = find(uf[x],uf)
    return uf[x]

def union(a,b,uf):
    a = find(a, uf)
    b = find(b, uf)
    if a < b:
        uf[b] = a
    else:
        uf[a] = b

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        uf = [j for j in range(n+1)]
        curr = [wires[j] for j in range(len(wires)) if j!=i]
        for a, b in curr:
            union(a, b, uf)
        for i in range(1,n+1):
            find(i, uf)
        uf = uf[1:]
        if len(set(uf)) == 2:
            answer = min(abs(uf.count(min(uf))-uf.count(max(uf))), answer)
    return answer