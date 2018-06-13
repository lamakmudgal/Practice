from urllib.request import urlopen

def readandprint();
    with urlopen ("http://www.archhousing.org/homebuyers/affordable-homes-sale.html") as web_file:
        print(web_file)
    ##ah = open("affordablehouses.txt", 'w')
    #for line in web_file:
    #    if("Bellevue") in str(line):

if __name__ == "__main__":
    readandprint()
