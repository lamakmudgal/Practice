# 1,1,2,3,5,8,13,21,
def fibnum(n,known_results):
	# base case 0 and 1 as the value is one.
	if n < 2:
		return 1
	if known_results[n] > 0:
		return known_results[n]
	else:
		known_results[n] = ?
	
	val =  fibnum(n-1,known_results)+fibnum(n-2,known_results)
	known_results[n] = val
	return val

def roll():
	val = random.randint(1,7)
	if val > 5:
		roll()
	return val

def roll_5():
	return random.randint(1,5)
	
def roll5_7()
	while True:
		
		roll1 = (roll_5()-1)*5
		roll2 = roll_5()
		
		if (roll1+roll2) > 21:
			pass
		else:
			return (roll1+roll2)%7+1

def findsqrt(n):
	if num < 0:
		return ValueError
	
	if num ==1:
		return 1

	for i in range(1,n//2+1):
		if i*i == n:
			return i
		elif i>n:
			return i -1
k = [1,5,6,21,33,44,45,46,56,67,78,88,89,99,101,109,123]
def searchnumber(num,sorted_arr):
	low = 0
	high = len(k)
	while low+1 < high :
		mid  = low + (high-low)//2
		
		if sorted_arr[mid] == num:
			return mid
		elif sorted_arr[mid] < num:
			low = mid
		else: 
			high = mid
			
list [1,2,3] [3,4,2,5,6,7] [-4,-2,5,6,6,4]	

target = 15 arr_coin = [1,5,10]
def findmindenom(target, arr_coin):
	mincoins = target
	if mincoins in arr_coin:
		return 1
	
	for i in arr_coin:
		numofcoins = 1+ findmindenom(target-i,arr_coin)
		if mincoins > numofcoins:
			mincoins = numofcoins
	return mincoins
		
		
	
		
		
	
		
	