x =[-1,-1,-1,0,0,1,1,1]
y =[-1,0,1,-1,1,-1,0,1]

def search2d(arr,row,col,word):
    #print(row,col,word)
    # check null condition
    if len(word)<1:
        print("found word",row,col)
        return True

    for direction in range(0,8):
        #print(direction)
        curr_row = row+x[direction]
        curr_col = col+y[direction]
        #print("curr_row,curr_col", curr_row, curr_col)
        if curr_row > len(arr) - 1 or curr_col > len(arr[0]) - 1 or curr_row < 0 or curr_col < 0:
            pass
            #print("Out of index curr_row,curr_col", curr_row, curr_col)
        else:
            if arr[curr_row][curr_col] == word[0]:
                search2d(arr,curr_row,curr_col,word[1:])
    return False



def find_word_grid(arr,word):
    for row in range(0,len(arr)):
        for col in range(0,len(arr[0])):
            #print(arr[row][col])
            if arr[row][col]==word[0]:
                print("search Called",row,col)
                search2d(arr,row,col,word[1:])

grid = [["g","e","e","k","g","g","r","g","e","e","k"],
        ["e","r","t","e","a","k","e","a","m","a","l"],
        ["k","e","e","a","m","e","w","l","a","t","m"],
        ["e","k","t","l","a","l","w","e","k","t","m"]]
print(find_word_grid(grid,"kamal"))