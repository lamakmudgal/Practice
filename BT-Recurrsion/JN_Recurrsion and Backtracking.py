if __name__ == '__main__':

    def printperm_duplicates(arr,l,r):
        """This function print permutation of a string without duplicates"""
        if l == r: # Print after the last swap in every iteration
            print(arr)
        else:
            for i in range(l,r+1):
                print(arr,l,r)
                if arr[i] not in arr[l:i]: # to check if the character is already covered.If repeated do not swap
                    arr[l],arr[i] = arr[i],arr[l]
                    printperm_duplicates(arr,l+1,r)
                    arr[l],arr[i] = arr[i],arr[l]
            print(l,r)
    arr = [1,2,3]
    #printperm_duplicates(arr,0,len(arr)-1)


    def count(coinarr, m, total,result):

        # If n is 0 then there is 1 solution (do not include any coin)
        if (total == 0):
            return 1

        # If n is less than 0 then no solution exists
        if (total < 0):
            return 0

        # If there are no coins and n is greater than 0, then no solution exist
        if (m <=0 and total >= 1):
            return 0

        # count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1] result= [0]
        val = count(coinarr, m - 1, total,result)
        result.add(coinarr[m-1])
        val += count( coinarr, m, total-coinarr[m-1],result)
        return val

    # Driver program to test above function
    arr = [1,5,10]
    m = len(arr)
    result ={0}
    print("Coins",count(arr, m, 100,result))


    def coinchange(coins,target,result,intrim):
        for i in coins:
            if i == target:
                #print("sucess",i,target)
                intrim =intrim+[i]
                #intrim.sort()
                if intrim is not None:
                    res.add(tuple(intrim))
                return
            elif target>i:
                coinchange(coins,target-i,result,intrim+[i])
            else:
                return
    coins =[5,10]
    res = set()
    target = 100
    intrim = []
    #coinchange(coins,target,res,intrim)
    #print(len(res))
