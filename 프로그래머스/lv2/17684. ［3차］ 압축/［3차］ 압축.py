def solution(msg):
    dic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
    dic_index = 27
    if len(msg) == 1:
        return [dic.get(msg[0])]
    prev = msg[0]
    answer = []
    for now in msg[1:]:
        pn = prev+now
        get_pn = dic.get(pn)
        if not get_pn:
            dic.update({pn : dic_index})
            dic_index += 1
            answer.append(dic.get(prev))
            prev = now
        else:
            prev += now
    else:
        if get_pn:
            answer.append(get_pn)
        else:
            answer.append(dic.get(now))
    return answer