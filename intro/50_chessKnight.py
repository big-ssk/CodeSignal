def chessKnight(cell):
    
    counter = 0
    board = [[0 for j in range(12)] for i in range(12)]
    letters = '__abcdefgh'
    
    x, y = letters.index(cell[0]), 10 - int(cell[1])
    moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    
    for i, j in moves:
        board[y + i][x + j] = 1

    for i in range(2, 10):
        for j in range(2, 10):
            if board[i][j] == 1:
                counter += 1
    
    return counter

