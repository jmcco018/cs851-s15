import random
import os
import math
import statistics

file=open("urissort",'r')
lines=file.readlines()

alluris=list()
warcreate=list()
wget=list()
webrecorder=list()
methods=['warcreate','wget','webrecorder']
for line in lines:
    urisizes=list()
    folder=line.rstrip().split(" ");
    for method in methods:
        try:
          loc='/home/jmcconne/cs751/a2/warcs/'+folder[1]+'/'+method+'/'
          files=os.listdir(loc)
          for f in files:
              if "warc.gz" in f:
                size=os.path.getsize(loc+f)
                print (loc+f+str(size))
                info=folder[1]+" "+method+" "+str(size)
                urisizes.append(info)
                if method == "warcreate":
                    warcreate.append(size)
                elif method == "wget":
                    wget.append(size)
                elif method == "webrecorder":
                    webrecorder.append(size)
                break
        except:
           print("NO") 
    alluris.append(urisizes)

print("warcreate")
totalwc=sum(warcreate)
itemswc=len(warcreate)
meanwc=statistics.mean(warcreate)
medianwc=statistics.median(warcreate)
print( "SUM: ",totalwc)
print( "LENGTH: ",itemswc)
print( "MEAN: ",meanwc)
print( "MEDIAN: ",medianwc)
    
print("wget")
totalwg=sum(wget)
itemswg=len(wget)
meanwg=statistics.mean(wget)
medianwg=statistics.median(wget)
print( "SUM: ",totalwg)
print( "LENGTH: ",itemswg)
print( "MEAN: ",meanwg)
print( "MEDIAN: ",medianwg)

print("Webrecorder")
totalwr=sum(webrecorder)
itemswr=len(webrecorder)
meanwr=statistics.mean(webrecorder)
medianwr=statistics.median(webrecorder)
print( "SUM: ",totalwr)
print( "LENGTH: ",itemswr)
print( "MEAN: ",meanwr)
print( "MEDIAN: ",medianwr)
