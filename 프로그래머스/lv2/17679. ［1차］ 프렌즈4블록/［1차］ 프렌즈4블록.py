def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    crash = set()

    while True:
        # 블록 충돌 검사
        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] != 0 and board[row][col] == board[row + 1][col] == board[row][col + 1] == board[row + 1][col + 1]:
                    crash.update([(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)])

        if not crash:
            break

        # 충돌한 블록 제거 및 아래로 이동
        for row, col in crash:
            board[row][col] = 0
        for col in range(n):
            cnt = 0
            for row in range(m - 1, -1, -1):
                if board[row][col] == 0:
                    cnt += 1
                else:
                    board[row][col], board[row + cnt][col] = board[row + cnt][col], board[row][col]

        answer += len(crash)
        crash = set()

    return answer