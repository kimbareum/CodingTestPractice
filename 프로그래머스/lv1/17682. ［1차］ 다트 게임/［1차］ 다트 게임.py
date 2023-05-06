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