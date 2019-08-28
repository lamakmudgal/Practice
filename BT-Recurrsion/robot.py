def getpath(maze):
    if maze == None or len(maze) == 0 :
        return None
    path = []
    catchedict = {}
    if ispath(maze, len(maze)-1, len(maze[0])-1, path,catchedict):
        return path
    else:
        return None
def ispath(maze, row, col, path,catchedict):
    if col<0 or row < 0 or not maze[row][col]:
        return False
    point = (row,col)
    if point in catchedict:
        return catchedict[point]
    sucess = False

    isatorifin = (row==0) and (col==0)
    if isatorifin or ispath(maze, row-1,col,path,catchedict) or ispath(maze,row,col-1,path,catchedict):
        point= (row,col)
        path.append(point)
        sucess =  True
    catchedict[point] = "True"
    print(catchedict)
    return sucess


if __name__ == "__main__":
    maze  = [[True,True,True, True],[True,True,True, True],[True,True,True, True],[True,True,True, True],[True,True,True, True]]
    print(getpath(maze))