oldkey = "2-5g-3-J"
k = 2
#remove dash
#oldkey = oldkey.replace("-","")
#oldkey = oldkey.upper()
#print(oldkey)
newstring=""
count = 0
for i in range(len(oldkey)-1,-1,-1):
    print(oldkey[i])
    if oldkey[i] == "-":
        pass
    else:
        if count == k:
            count = 0
            newstring = "-"+newstring
        count = count +1
        newstring = oldkey[i].upper() + newstring

print("newstring",newstring)


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        output = []
        modifiedString = S.replace('-', "").upper()
        length = len(modifiedString)
        i = 0
        if length % K != 0:
            remainder = length % K
            output.append(modifiedString[i:remainder])
            i = remainder
        while i < length:
            output.append(modifiedString[i:i + K])
            i += K

        return "-".join(output)

