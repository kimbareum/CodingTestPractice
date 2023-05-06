def solution(dart_result):
    dart_score, dart_val = [], []
    temp_score, temp_val = '', ''
    for i in dart_result:
        if i.isdigit() == False:
            if temp_score != '':
                dart_score.append(int(temp_score))
                temp_score = ''
            temp_val += i
        else :
            if temp_val != '':
                dart_val.append(temp_val)
                temp_val = ''
            temp_score += i
    else:
        dart_val.append(temp_val)
    for i in range(len(dart_score)):
        if dart_val[i][0] == 'T':
                dart_score[i] **= 3
        elif dart_val[i][0] == 'D':
            dart_score[i] **= 2
        if len(dart_val[i]) == 2:
            if dart_val[i][1] == '#':
                dart_score[i] = -dart_score[i]
            else:
                if i != 0 :
                    dart_score[i-1] *= 2
                dart_score[i] *= 2    
    return(sum(dart_score))


# p = re.compile('(\d+)([SDT])([*#]?)')
# dart = p.findall(dartResult)
# 정규표현식으로 구성한 compile과 findall 조합하면
# [('1', 'S', '*'), ('2', 'T', '*'), ('3', 'S', '')]
# 이런 형태로 만들어 줌.
