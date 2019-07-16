import heapq

fp = open("billionnum.txt")
heaparr = []
fileended = False
while fileended == False:
    for i in range(100):
        val = fp.readline()
        print("val:-",val)
        if val == "":
            print("file ended")
            fileended = True
            break
        heaparr.append(int(val)*(-1))
    #print(heaparr)
    heapq.heapify(heaparr)
    top10 = []
    for i in range(10):
        top10.append(heapq.heappop(heaparr))
    #print(top10)
    heaparr.clear()
    heaparr = top10
    print(heaparr)
