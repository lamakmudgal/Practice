N=4
# A utility function to print solution matrix sol
def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


# A utility function to check if x, y is valid
# index for N * N Maze
def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False



def solvemaze(maze):
    # Creating a 4 * 4 2-D list
    sol = [[0 for j in range(4)] for i in range(4)]

    if solvemazerecur(maze,0,0,sol) is False:
        print("No solution")
        return False
    printSolution(sol)
    return True

def solvemazerecur(maze,row,col,sol):
    if row == len(maze)-1 and col == len(maze)-1 :
        return True


    if isSafe(maze,row,col):
        sol[row][col] =1

        if solvemazerecur(maze,row+1,col,sol) is True:
            return True

        if solvemazerecur(maze,row,col+1,sol) is True:
            return True

        sol[row][col] = 0
        return False

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

solvemaze(maze)