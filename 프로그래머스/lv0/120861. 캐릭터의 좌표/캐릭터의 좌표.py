def solution(keyinput, board):
    commands = {"left": (-1,0), "right":(1,0), "up":(0,1), "down":(0,-1)}
    answer = [0,0]
    width, height = board[0]//2, board[1]//2
    for key in keyinput:
        move = commands.get(key)
        if (answer[0] + move[0] > width or answer[0] + move[0] < -width) or\
        (answer[1] + move[1] > height or answer[1] + move[1] < -height):
            continue
        else :
            answer[0] += move[0]
            answer[1] += move[1]
    return answer