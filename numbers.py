input_string = input("Please enter a string which can be palindrome or not.")
input_string = input_string.strip()
print(input_string)
stringlist = list(input_string)
print("list of string",stringlist)
print("Length of string",len(stringlist))
for i in range(0,len(stringlist)):
    if (stringlist[i] == stringlist[len(stringlist)-(i+1)]):
        pass
    else:
        print("not a palindrome")
        break
    print("Palindrome")
    break




