def findislandhelper(input_arr,visited):
    adjacent_row = [-1,-1,-1, 0,0, 1,1,1]
    adjacent_col = [-1, 0, 1,-1,1,-1,0,1]
    count = 0
    for curr_row in range(0,len(input_arr)):
        for curr_col in range(0,len(input_arr[0])):
            if visited[curr_row][curr_col] != 1:
                count += findisland(input_arr,adjacent_row,adjacent_col,curr_col,curr_row,visited)
    return count


def findisland(input_arr,adjacent_row,adjacent_col,curr_col,curr_row,visited):
    if visited[curr_col][curr_row] != 1:
        if input_arr[curr_col][curr_row] == 0:
            visited[curr_col][curr_row] = 1
            return 0

        if input_arr[curr_col][curr_row] == 1:
            visited[curr_col][curr_row] = 1
            for i in range(0,8):
                next_col = curr_col + adjacent_col[i]
                next_row = curr_row + adjacent_row[i]
                # check if location is valid or not.
                if next_row > -1 and next_col > -1 and next_row < len(input_arr) and next_col < len(input_arr[0]):
                    if visited[next_col][next_row] != 1:
                        findisland(input_arr, adjacent_row, adjacent_col, next_col,next_row, visited)
            return 1
    else:
        return 0

input_arr = [[0,0,1,0],
             [0,0,0,1],
             [0,0,1,0],
             [0,0,0,1]]
visited = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
           [0,0,0,0]]

print("count of island",findislandhelper(input_arr,visited))