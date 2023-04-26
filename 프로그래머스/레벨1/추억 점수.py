def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    dic = dict(zip(name,yearning))
    for i in range(len(photo)):
        for j in photo[i]:
            try :
                answer[i] += dic[j]
            except:
                continue
    return answer