import os.path, glob,sys
from shutil import copyfile

#Get the scenario name from maps to create the log file with the name
listofArguments = []
listofArguments = sys.argv
scenario = str(listofArguments).split()
scenario_name = str(listofArguments[3])
callNumber = ""
wFile = open('C:\\NGQA\\ETHOS-LCU\\Logs\\xSwitch-'+scenario_name+'.log', 'w',  newline='')

Flag1=False
dir = r'C:\Program Files (x86)\microDATA\xSwitch\Logs\xSwitch*'
#print (dir)

#gets the latest 5 files and saves it in a dict - File
LatestFile = sorted(glob.iglob(dir), key=os.path.getctime,reverse=True)
len1=len(LatestFile)
print (len1)
wFile.write("The number of files are: - "+str(len1)+'\n')
File={}
if len1 < 6:
	for i in range(1, len1):
		File.update({"File"+str(i) : LatestFile[i-1]})
else:
	for i in range(1,6):
		File.update({"File"+str(i) : LatestFile[i-1]})

#Iterate through the latest file and get the callID
with open(File["File1"], "r") as rfile:
    lines=rfile.readlines()
    for eachline in lines:
        if "####" in str(eachline) and Flag1==False:
            Flag1=True
            word = eachline.split()
            callNumber = str(word[8])
            print (callNumber)
            rfile.close()
            break
	if (callNumber == ""):
		wfile.write("The call ID was not found in latest files.)



#create the Log file
for files in sorted(list(File.keys()),reverse=True):
    with open(File[files], "r") as r1file:
        lines1 = r1file.readlines()
        for eachline1 in lines1:
            if callNumber in str(eachline1):
                wFile.write(eachline1)


r1file.close()
wFile.close()