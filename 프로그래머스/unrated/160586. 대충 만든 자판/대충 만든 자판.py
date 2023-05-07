def solution(keymap, targets):
    keymapSet = set([i for i in str(keymap) if i not in ["[","]",","," ","","\'"]])
    keymapDic = dict()
    answer = []
    for i in keymapSet:
        temp = 101
        for j in keymap:
            temp2 = j.find(i)+1
            if temp2 != 0 and temp2 < temp:
                temp = temp2
        keymapDic.update({i : temp})
    for i in targets:
        if set(i).issubset(keymapSet):
            temp = 0
            for j in i:
                temp += keymapDic[j]
        else:
            temp = -1
        answer.append(temp)
                
    return answer