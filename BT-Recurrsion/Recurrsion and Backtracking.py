#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def printperm_duplicates(arr,l,r):    
    if l == r:
        print(arr)       
    else:
        for i in range(l,r+1):
            print(arr,l,r)
            if arr[i] not in arr[l:i]: # to check if the repetion is already covered.If repeated dont swap
                arr[l],arr[i] = arr[i],arr[l]
                printperm_duplicates(arr,l+1,r)
                arr[l],arr[i] = arr[i],arr[l]
        print(l,r)
arr = [1,2,3]
printperm_duplicates(arr,0,len(arr)-1)

# In[ ]:
def printperm(arr,l,r):
    #print("Printed that",arr,l,r) 
    if l == r: # Print after the last swap in every iteration
        print(arr)            
    for i in range(l,r+1):
        if arr[i] not in arr[l:i]:
            arr[l],arr[i] = arr[i],arr[l]
            printperm(arr,l+1,r)
            arr[l],arr[i] = arr[i],arr[l]
    if r-l == len(arr)-1 and 1 not in arr: # This check makes sure that the permutation of earlier array has been printed
        print("adding one")
        for i in range(0,len(arr)):
            arr[i] = 1
            printperm(arr,l,r)
    #print("Printed this",arr,l,r)   
arr = [0,0,0,0,0,0]
printperm(arr,0,len(arr)-1)


# In[ ]:


def nsizedstring(n,k,mystr):
    if n<=0:
        print(arr)
        return
    for i in range(0,k):
        #print()
        print("value to input",chr(i+ord('0')))
        mystr[n-1] = chr(i+ord('0'))
        nsizedstring(n-1,k,mystr)
arr = [0,0,0,0]
nsizedstring(4,2,arr)


# In[4]:


def count(coinarr, m, total,result): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (total == 0): 
        #print(result)
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (total < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and total >= 1): 
        #result= result[:-1]
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    #esult= [0]
    val = count( coinarr, m - 1, total,result)
    result.add(coinarr[m-1])
    val += count( coinarr, m, total-coinarr[m-1],result)
    return val
  
# Driver program to test above function 
arr = [1,5,10,25,50] 
m = len(arr) 
result ={0}
print(count(arr, m, 100,result)) 


# In[7]:


def coinchange(coins,target,result,intrim):
    for i in coins:
        if i == target:
            #print("sucess",i,target)
            intrim =intrim+[i]
            intrim.sort()
            if intrim is not None:
                res.add(tuple(intrim))
            return
        elif target>i:
            coinchange(coins,target-i,result,intrim+[i])
        else:
            return
coins =[5,10,25,50]
res = set()
target = 100
intrim = []
coinchange(coins,target,res,intrim)
print(res,len(res))


# In[2]:


def findislandhelper(input_arr,visited):
    adjacent_row = [-1,-1,-1, 0,0, 1,1,1]
    adjacent_col = [-1, 0, 1,-1,1,-1,0,1]
    count = 0
    for curr_row in range(0,len(input_arr)):
        for curr_col in range(0,len(input_arr[0])):
            if visited[curr_row][curr_col] != 1:
                #visited[curr_row][curr_col] = 1
                #print("visitedarray",visited)
                count += findisland(input_arr,adjacent_row,adjacent_col,curr_col,curr_row,visited)
                print("visitedarray after neighbour check", visited)
            else:
                print("already visited")
    return count

def findisland(input_arr,adjacent_row,adjacent_col,curr_col,curr_row,visited):
    print("row-col",curr_col,curr_row,"visited",visited)
    if visited[curr_col][curr_row] != 1:
        if input_arr[curr_col][curr_row] == 0:
            visited[curr_col][curr_row] = 1
            print("found zero",curr_col,curr_row)
            return 0

        if input_arr[curr_col][curr_row] == 1:
            print("found 1 checking neighbours")
            visited[curr_col][curr_row] = 1
            for i in range(0,8):
                next_col = curr_col + adjacent_col[i]
                next_row = curr_row + adjacent_row[i]
                print("in for loop", next_col, next_row)
                if next_row > -1 and next_col > -1 and next_row < len(input_arr) and next_col < len(input_arr[0]):
                    if visited[next_col][next_row] != 1:
                        findisland(input_arr, adjacent_row, adjacent_col, next_col,next_row, visited)
                    else:
                        print("visited go next")
                else:
                     print("out of index",next_col,next_row)
                print("visited in for loop",visited,next_col,next_row)
            return 1
    else:
        print("already visited find island func")
        return 0

"""
input_arr = [
       [0,1,1,1,1],
       [1,1,0,0,1],
       [1,0,0,1,0],
       [0,0,0,0,0],
       [1,1,1,1,1]
    ]
visited = [
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
"""
input_arr = [[1,0,1,0],
             [0,0,0,1],
             [1,0,1,0],
             [0,0,0,1]]
visited = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
           [0,0,0,0]]

print("count of island",findislandhelper(input_arr,visited))


#!/usr/bin/env python
# coding: utf-8

# In[4]:


# A Backtracking program  in Python to solve Sudoku problem 
# A Utility Function to print the Grid 
def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j],end="") 
        print ('n') 
# Function to Find the entry in the Grid that is still  not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remain, false is returned. 
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
# Checks whether it will be legal to assign num to the given row,col 
#  Returns a boolean which indicates whether it will be legal to assign 
#  num to the given row,col location. 
def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(arr,row,col,num)): 
              
            # make tentative assignment 
            arr[row][col]=num 
  
            # return, if success, ya! 
            if(solve_sudoku(arr)): 
                return True
  
            # failure, unmake & try again 
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False 
  
# Driver main function to test above functions 
if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid=[[0 for x in range(9)]for y in range(9)] 
      
    # assigning values to the grid 
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
      
    # if success print the grid 
    if(solve_sudoku(grid)): 
        print_grid(grid) 
    else: 
        print ("No solution exists")


# In[1]:


arr = [[1,2,3],
      ["a","b","c"]]
print(arr[0][1])



