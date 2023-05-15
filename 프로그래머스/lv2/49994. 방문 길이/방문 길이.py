def solution(dirs):
    visited = set()
    commands = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    x1, y1 = 0, 0
    for i in dirs:
        x2, y2 = x1 + commands[i][0], y1+ commands[i][1]
        if  -5 <= x2 <= 5 and -5 <= y2 <= 5:
            visited.add(((x1,y1), (x2,y2)))
            visited.add(((x2,y2), (x1,y1)))
            x1, y1 = x2, y2
    return len(visited)//2