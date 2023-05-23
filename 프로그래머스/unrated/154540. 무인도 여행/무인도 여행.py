def solution(maps):
    answer = []

    stack2 = []
    visited = set()
    rows, cols = len(maps), len(maps[0])
    for row in range(rows):
        for col in range(cols):
            # 'X' 가 아닌 위치 찾기
            if maps[row][col] != 'X':
                stack = [(row,col)]
                # 이미 방문했다면 탐색하지않음
                if stack[-1] in visited:
                    stack.pop()
                    continue
                # 방문하지 않았다면 주변 탐색
                temp = 0
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        data = maps[curr[0]][curr[1]]
                        if data != 'X':
                            temp += int(data)
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                new_row, new_col = curr[0] + dx, curr[1] + dy
                                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                                    stack.append((new_row, new_col))
                        visited.add(curr)
                if temp:
                    answer.append(temp)
    return sorted(answer) if answer else [-1]