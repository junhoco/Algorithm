def solution(keyinput, board):
    maxLR = board[0] // 2
    maxUD = board[1] // 2
    res = [0] * 2
    for key in keyinput:
        if key == 'left':
            res[0] -= 1
        elif key == 'right':
            res[0] += 1
        elif key == 'up':
            res[1] += 1
        else:
            res[1] -= 1
        
        if key == 'left' and res[0] < -(maxLR):
            res[0] = -(maxLR)
        elif key == 'left' and res[0] > maxLR:
            res[0] = maxLR
        elif key == 'right' and res[0] < -(maxLR):
            res[0] = -(maxLR)
        elif key == 'right' and res[0] > maxLR:
            res[0] = maxLR
        elif key == 'down' and res[1] < -(maxUD):
            res[1] = -(maxUD)
        elif key == 'down' and res[1] > maxUD:
            res[1] = maxUD
        elif key == 'up' and res[1] < -(maxUD):
            res[1] = maxUD
        elif key == 'up' and res[1] > maxUD:
            res[1] = maxUD
    return res