def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int,today.split('.'))
    today = (year-2000)*28*12+(month-1)*28+day
    termsDic = dict()
    for i in terms:
        term, period = i.split()
        termsDic.update({term:int(period)})
    for i in range(len(privacies)):
        start, term = privacies[i].split()
        year2, month2, day2 = map(int,start.split('.'))
        month2 += termsDic.get(term)
        day2 -= 1
        eDay = (year2-2000)*28*12+(month2-1)*28+day2
        if eDay < today:
            answer.append(i+1)
    return answer