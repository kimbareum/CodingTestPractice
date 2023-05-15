def solution(fees, records):
    total_time = dict()
    queue = dict()
    for i in records:
        time, number, flag = i.split()
        time = (lambda x : int(x[0])*60 + int(x[1]))(time.split(':'))
        if number in queue:
            parking_time = time-queue.pop(number)    
            total_time.update({number : parking_time + total_time.get(number,0)})
        else:
            queue.update({number : time})
    else :
        while queue:
            number, time = queue.popitem()
            parking_time = 1439-time
            total_time.update({number : parking_time + total_time.get(number,0)})
    total_time = sorted(total_time.items())
    answer = []
    for _ , time in total_time:
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]-(-(time-fees[0])//fees[2])*fees[3])
    return answer