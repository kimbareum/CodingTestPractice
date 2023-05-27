def solution(places):
    answer = []
    for room in places:
        p = []
        for row in range(5):
            for col in range(5):
                if room[row][col] == 'P':
                    p.append((row,col))
        flag = 0
        for i in range(len(p)-1):
            if flag == 1:
                break
            for j in range(i+1,len(p)):
                (row1, col1) = p[i]
                (row2, col2) = p[j]
                distance = abs(row1-row2)+ abs(col1-col2)
                if distance <= 2:
                    if distance == 1:
                        flag = 1
                    elif abs(row1 - row2) == 2:
                        if room[(row1 + row2)//2][col1] != 'X':
                            flag = 1
                    elif abs(col1 - col2) == 2 :
                        if room[row1][(col1+col2)//2] != 'X':
                            flag = 1     
                    else:
                        if room[row1][col2] != 'X' or room[row2][col1] != 'X':
                            flag = 1
                    if flag == 1:
                        answer.append(0)
                        break
        if flag == 0:
            answer.append(1)
    return answer