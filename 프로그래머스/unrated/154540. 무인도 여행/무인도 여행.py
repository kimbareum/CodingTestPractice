def solution(maps):
    answer = []
    stack = []
    stack2 = []
    visited = set()
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] != 'X':
                stack.append((row,col))
    while stack:
        if stack[-1] in visited:
            stack.pop()
            continue
        stack2.append(stack.pop())
        temp = 0
        while stack2:
            curr = stack2.pop()
            if curr not in visited:
                data = maps[curr[0]][curr[1]]
                if data != 'X':
                    temp += int(data)
                    if 0 <= curr[0]-1 and (curr[0]-1, curr[1]) not in visited:
                        stack2.append((curr[0]-1, curr[1]))
                    if 0 <= curr[1]-1 and (curr[0], curr[1]-1) not in visited:
                        stack2.append((curr[0], curr[1]-1))
                    if curr[0]+1 < len(maps) and (curr[0]+1, curr[1]) not in visited:
                        stack2.append((curr[0]+1, curr[1]))
                    if curr[1]+1 < len(maps[0]) and (curr[0], curr[1]+1) not in visited:
                        stack2.append((curr[0], curr[1]+1))
                visited.add(curr)
        if temp:
            answer.append(temp)
    return sorted(answer) if answer else [-1]