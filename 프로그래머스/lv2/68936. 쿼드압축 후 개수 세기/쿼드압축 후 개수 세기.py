from collections import deque
def solution(arr):
    arr_len = len(arr)
    answer = [0,0]
    #x1, y1, x2, y2
    queue = deque([[0, 0, arr_len-1, arr_len-1]])
    while queue:
        y1, x1, y2, x2 = queue.popleft()
        temp = []
        for row in range(y1,y2+1):
            temp.extend(arr[row][x1:x2+1])
        if all(temp):
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    if x == x1 and y == y1:
                        continue
                    arr[y][x] = -1
            continue
        elif any(temp):
            pass
        else:
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    if x == x1 and y == y1:
                        continue
                    arr[y][x] = -1
            continue 
        ymid = y1+(y2-y1)//2
        xmid = x1+(x2-x1)//2
        queue.append([y1, x1, ymid, xmid])
        queue.append([y1, xmid+1, ymid, x2])
        queue.append([ymid+1, x1, y2, xmid])
        queue.append([ymid+1, xmid+1, y2, x2])
    for row in arr:
        answer[0] += row.count(0)
        answer[1] += row.count(1)
    return answer
