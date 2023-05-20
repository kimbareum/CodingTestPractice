from collections import deque
def solution(arr):
    arr_len = len(arr)
    answer = [0,0]
    #x1, y1, x2, y2
    queue = deque([[0, 0, arr_len-1, arr_len-1]])
    while queue:
        y1, x1, y2, x2 = queue.popleft()
        if x1 == x2 and y1 == y2:
            answer[arr[y1][x1]] += 1
            continue
        first = arr[y1][x1]
        break_flag = 0
        for row in range(y1,y2+1):
            for col in range(x1,x2+1):
                if arr[row][col] != first:
                    break_flag = 1
                    break
            if break_flag == 1:
                break
        else:
            answer[first] += 1
            continue
        ymid = y1+(y2-y1)//2
        xmid = x1+(x2-x1)//2
        queue.append([y1, x1, ymid, xmid])
        queue.append([y1, xmid+1, ymid, x2])
        queue.append([ymid+1, x1, y2, xmid])
        queue.append([ymid+1, xmid+1, y2, x2])
    return answer
