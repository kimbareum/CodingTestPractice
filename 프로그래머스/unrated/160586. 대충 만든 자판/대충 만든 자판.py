def solution(keymap, targets):
    keymapSet = set([i for i in str(keymap) if i not in ["[","]",","," ","","\'"]])
    keymapDic = dict()
    answer = []
    for i in keymapSet:
        min_press = 101
        for j in keymap:
            key_press = j.find(i)+1
            if key_press != 0 and key_press < min_press:
                min_press = key_press
        keymapDic.update({i : min_press})
    for i in targets:
        if set(i).issubset(keymapSet):
            press = 0
            for j in i:
                press += keymapDic[j]
        else:
            press = -1
        answer.append(press)
                
    return answer