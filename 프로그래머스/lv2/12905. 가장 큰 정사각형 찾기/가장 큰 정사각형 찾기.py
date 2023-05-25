def solution(board):
    # DP 문제
    answer = 0
    width, height = len(board[0]), len(board)
    lengths = [[0 for _ in range(width+1)] for i in range(height+1)]
    for row in range(1,height+1):
        for col in range(1, width+1):
            if board[row-1][col-1] == 1:
                lengths[row][col] = 1+ min(lengths[row-1][col],
                                           lengths[row][col-1],
                                           lengths[row-1][col-1])
            if lengths[row][col] > answer:
                answer = lengths[row][col]
    return answer ** 2