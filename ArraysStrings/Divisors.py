number = int(input("Please enter the number if its prime or find its divisors : - "))

possibledivisors = range(2,int(number)+1)
divisor = [x for x in possibledivisors if number%x == 0]
#for x in possibledivisors:
#    print("X is :- ", number%x)
#    if ((number%x) == 0):
#        divisor.append(x)
if len(divisor) == 1:
    print("Its is prime number")
    print(divisor)
else:
    print(divisor)