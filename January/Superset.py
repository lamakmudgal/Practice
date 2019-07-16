def getsubsets(baseset,index):
    print("getsubsetcall",index)
    allsubset = []
    if index == 0:
       if [] not in allsubset:
           allsubset.append([])
    else:
        allsubset = getsubsets(baseset,index-1)
        moresubset = []
        value = baseset[index-1]
        print(value)
        for subset in allsubset:
            newsubset= []
            for eachval in subset:
                if eachval not in newsubset:
                    newsubset.append(eachval)
            newsubset.append(value)
            moresubset.append(newsubset)
        print("moresubset",moresubset)
        for item in moresubset:
            if item not in allsubset:
                allsubset.append(item)
    print("return")
    return allsubset

print("Calculate subset")
print(getsubsets([1,2,3],len([1,2,3])))