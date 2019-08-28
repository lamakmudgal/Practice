number_iterations = "2,8"#input("Enter the start point and iteration for fibonacci series (comma separated)")
number_iterations = number_iterations.split(",")
fib= [int(number_iterations[0])]
for i in range (1,int(number_iterations[1])):
    if i < 2:
        fib.append(fib[0])
    else:
        fib.append(fib[-1]+fib[-2])
print(fib)