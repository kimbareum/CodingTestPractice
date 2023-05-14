def solution(n, t, m, p):
    answer = ''
    base = dict(zip(range(n+1),'0123456789ABCDEF'))
    all_num = '0'
    cnt = 1
    while len(all_num) < t*m:
        temp = ''
        num = cnt
        while num > 0:
            num, mod = divmod(num, n)
            temp = base.get(mod)+temp
        all_num += temp
        cnt += 1
    for i in range(p-1,t*m,m):
        answer += all_num[i]
    return answer