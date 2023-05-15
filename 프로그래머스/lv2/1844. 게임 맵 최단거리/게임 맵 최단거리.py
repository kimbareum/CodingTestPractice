from collections import deque
def solution(maps):
    height = len(maps)
    width = len(maps[0])
    queue = deque([[0,0,1]])
    visited = set()
    while queue:
        row, col, dist= queue.popleft()
        if row == height - 1 and col == width - 1:
            return dist
        if (row, col) in visited:
            continue
        visited.add((row,col))
        if row > 0 and maps[row-1][col] >= 1:
            maps[row-1][col] = maps[row][col] + 1
            queue.append([row-1,col,dist+1])
        if col > 0 and maps[row][col-1] >= 1:
            maps[row][col-1] = maps[row][col] + 1
            queue.append([row,col-1,dist+1])
        if row < height-1 and maps[row+1][col] >= 1:
            maps[row+1][col] = maps[row][col] + 1
            queue.append([row+1,col,dist+1])
        if col < width-1 and maps[row][col+1] >= 1:
            maps[row][col+1] = maps[row][col] + 1
            queue.append([row,col+1,dist+1])

    return -1