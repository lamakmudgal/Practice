import time.sleep as sleep
import sys
import os
import shutil

for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)



#try:
#    while True:
        # code to find the latest file

        # code to copy it to another location

#        sleep(3600)
#except KeyboardInterrupt:
#    print("Quitting the program.")
#except:
#    print("Unexpected error: "+sys.exc_info()[0])
#    raise