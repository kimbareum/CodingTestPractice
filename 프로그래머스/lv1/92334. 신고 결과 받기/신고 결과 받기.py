def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reportedDic = dict().fromkeys(id_list, 0)
    reporterDic = {i:[] for i in id_list}
    for i in set(report):
        reporter, reported = i.split()
        reportedDic[reported] += 1
        reporterDic[reported].append(id_list.index(reporter))
    
    for person, cnt in reportedDic.items():
        if cnt >= k:
            for i in reporterDic[person]:
                answer[i] += 1       
    return answer