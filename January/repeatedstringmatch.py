"""
Problem:
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
Note:
The length of A and B will be between 1 and 10000.

Discussion: For B to be a substring of multiple of A it palindrom of A should exist in B.


Default cases:
 length of B should be greater than A

for

"""
# Solution

A = "abcd"
B = "cdabcdab"
i = 0
finalstring = ""
while len(finalstring) < len(B):
    finalstring = finalstring + A
    i = i + 1
print(finalstring,i)
if finalstring == B:
    print("inhere")
    print(i)
elif finalstring.find(B):
    print("inhere 2",finalstring,B)
    print(i)

print(finalstring.find(B))
print(finalstring.find("k"))
print(finalstring.find("ab"))

"""

elif (finalstring + A).find(B):
    print("inhere 3")
    print(i+1)
else:
    print("-1")

# if
"""