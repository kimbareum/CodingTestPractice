def solution(numbers, hand):
    loc = {1:(0,0), 2:(0,1), 3:(0,2),
            4:(1,0), 5:(1,1), 6:(1,2),
            7:(2,0), 8:(2,1), 9:(2,2),
            0:(3,1)}
    left, right = (3,0), (3,2)
    answer = ''
    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            left = loc[i]
        elif i in (3, 6, 9):
            answer += 'R'
            right = loc[i]
        else:
            left_len = abs(left[0]-loc[i][0])+abs(left[1]-loc[i][1])
            right_len = abs(right[0]-loc[i][0])+abs(right[1]-loc[i][1])
            if left_len < right_len:
                answer += 'L'
                left = loc[i]
            elif left_len > right_len:
                answer += 'R'
                right = loc[i]
            else:
                answer += hand[0].upper()
                if hand == "right":
                    right = loc[i]
                else:
                    left = loc[i]
    return answer