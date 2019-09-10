def rooksaresafe(board):  # Iterative solution.
    for i in range(0, len(board)):
        numofrooks = 0
        for j in board[i]:
            if j == 1:
                numofrooks += 1
                print(numofrooks)
            if numofrooks > 1:
                return False
        numofrookscol = 0
        for k in range(0, len(board)):
            if board[k][i] == 1:
                print("i,k,val:-", i, k, board[k][i])
                numofrookscol = numofrookscol+1
                print("Col", numofrookscol)
            if numofrookscol > 1:
                return False
    return True


board1 = [[1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]]
print(rooksaresafe(board1))
