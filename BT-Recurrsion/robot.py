def getpath(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    catchedict = {}
    if ispath(maze, len(maze)-1, len(maze[0])-1, path, catchedict):
        return path
    else:
        return None


def ispath(maze, row, col, path, catchedict):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    point = (row, col)
    if point in catchedict:
        return catchedict[point]
    success = False

    isatorifin = (row == 0) and (col == 0)
    if isatorifin or ispath(maze, row-1, col, path, catchedict) or ispath(maze, row,col-1,path,catchedict):
        point= (row,col)
        path.append(point)
        success = True
    catchedict[point] = True
    print(catchedict)
    return success


if __name__ == "__main__":
    maze1 = [[False, False, False, False],
             [False, False, True, True],
             [True, True, False, True],
             [True, True, True, True]]
    print(getpath(maze1))
