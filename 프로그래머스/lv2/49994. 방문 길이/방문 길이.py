def solution(dirs):
    answer = 0
    visited = set()
    commands = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    x1, y1 = 0, 0
    for i in dirs:
        command = commands[i]
        x2, y2 = x1 + command[0], y1+ command[1]
        if x2 > 5 or x2  < -5 or y2 > 5 or y2 < -5:
            continue
        if ((x1,y1), (x2,y2)) not in visited or ((x2,y2), (x1,y1)) not in visited:
            answer += 1
            visited.add(((x1,y1), (x2,y2)))
            visited.add(((x2,y2), (x1,y1)))
        x1, y1 = x2, y2
    return answer