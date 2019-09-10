"""
Print all possible words from phone digits
Before advent of QWERTY keyboards, texts and numbers were placed on the same key. For example 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once. If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. below is picture of such keypad.
https://www.geeksforgeeks.org/find-possible-words-phone-digits/
"""


def num_frm_digits_helper(digits):
    if digits is None:
        return
    curr = 0
    output = []
    n = len(digits)
    num_frm_digits(digits,curr,output,n)


def num_frm_digits(digits,curr,output,n):
    alphs = ["","","abc","def","ghi","jkl","mno","pqr"]
    if curr == n:
        print(output, curr, n)
        return

    for i in range(0,len(alphs[digits[curr]])):
        #print("length:-",len(alphs[digits[curr]]))
        output.append(alphs[digits[curr]][i])
        num_frm_digits(digits,curr+1,output,n)
        output.pop()
        #print(output,curr)
        #if (digits[curr] == 0 or digits[curr] == 1):
        #    return


digits = [2, 3, 4]
num_frm_digits_helper(digits)
