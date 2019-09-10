# Python3 program to find the smallest window
# containing all characters of a pattern.
no_of_chars = 256

# Function to find smallest window containing all characters of 'pat'
def findSubString(string, pat):
    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars
    for i in pat:
        hash_pat[ord(i)] += 1

    start = 0
    count = 0
    end = len(string) - 1
    minlenth = 1000
    res = ""

    for j in range(0, len(string)):
        # print(string[j])
        hash_pat[ord(string[j])] -= 1
        if hash_pat[ord(string[j])] >= 0:
            # print("found",string[j])
            count += 1
        while count == len(pat):
            print("first take", start)
            if minlenth > j - start + 1:
                minlenth = j - start + 1
                res = string[start:j + 1]
                print("Result:", res)
            hash_pat[ord(string[start])] += 1
            if hash_pat[ord(string[start])] > 0:
                print("here")
                count -= 1
            start += 1

    return res


# Driver code
if __name__ == "__main__":
    string = "cccaaaabweeefgewcwaefgcf"
    pat = "cae"

    print("Smallest window is : ")
    print(findSubString(string, pat))
