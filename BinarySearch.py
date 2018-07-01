def binarySearch (listofnumbersparameter,p_numbertobesearched):
    print(listofnumbersparameter)
    print(p_numbertobesearched)
    numberfound = True
    while (numberfound):
        lengthoflist = len(listofnumbersparameter)
        if(p_numbertobesearched == listofnumbersparameter[int(lengthoflist/2)]):
            print("Found the number its at location", int(lengthoflist/2))
            numberfound = False
        elif(p_numbertobesearched > listofnumbersparameter[int(lengthoflist/2)]):
            # Pick the right side of the list
            listofnumbersparameter = listofnumbersparameter[int(lengthoflist/2):]
            print("New list to compare is : - ", listofnumbersparameter)
        elif (p_numbertobesearched < listofnumbersparameter[int(lengthoflist/2)]):
            listofnumbersparameter = listofnumbersparameter[:int(lengthoflist / 2)]
            print("New list to compare is : - ",listofnumbersparameter)
        if(lengthoflist == 1):
            print("Number not in this list")
            numberfound = False




listofnumbers = [1,2,3,4,5,6,7,8,9]#input("Please enter a ordered list of numbers :- ")
numbertobesearched = int(input("Please enter a number to be searched in this list :- "))
binarySearch(listofnumbers,numbertobesearched)