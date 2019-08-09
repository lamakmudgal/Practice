grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
def printgrid(arr):
    for i in range(len(arr)):
        #print("|",end="")
        if i % 3 == 0:
            print("----------------")
        for j in range(len(arr[0])):
            if j%3==0:
                print("| ",end="")
            print(arr[i][j],end="")
        print(" |")

def check_row(row,num,arr):
    for i in range(0,9):
        if arr[row][i] == num:
            return False
    return True
def check_col(col,num,arr):
    for i in range(0,9):
        if arr[i][col] == num:
            return False
    return True
def check_box(row,col,num,arr):
    box_start_row = row-row%3
    box_start_col = col-col%3
    for i in range(box_start_row,box_start_row+3):
        for j in range(box_start_col,box_start_col+3):
            if arr[i][j] == num:
                return False
    return True 

def find_empty(arr,l):
    for i in range(0,9):
        for j in range(0,9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def check_safe_location(arr,row,col,num):
    return check_row(row,num,arr) and check_col(col,num,arr) and check_box(row,col,num,arr)

def solve_sudoku(arr):
    l=[0,0]
    if(not find_empty(arr,l)):
        return True
    print(l)
    row = l[0]
    col = l[1]

    for num in range(1,10):
        if check_safe_location(arr,row,col,num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True

            arr[row][col] = 0
    return False

solve_sudoku(grid)
printgrid(grid)

