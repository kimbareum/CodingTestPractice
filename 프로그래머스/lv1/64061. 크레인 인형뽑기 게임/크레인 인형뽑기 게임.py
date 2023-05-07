def solution(board, moves):
    answer = 0
    col = []
    basket = [0]
    for i in range(len(board[0])):
        temp = []
        for j in range(len(board)-1,-1,-1):
            k= board[j][i]
            if k != 0:
                temp.append(k)
        col.append(temp)
    # col = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    for i in moves:
        if len(col[i-1]) != 0:
            move = col[i-1].pop()
            if basket[-1] == move:
                basket.pop()
                answer += 2
            else:
                basket.append(move)
    return answer