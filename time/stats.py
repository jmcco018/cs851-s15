import statistics
import math

file=open('timedif','r')
strdeltas=file.readlines()
deltas=list()
total=0
medianvalue=0
meanvalue=0
stderrvalue=0
stddevvalue=0

for delta in strdeltas:
    deltas.append(int(delta.rstrip()))

total=sum(deltas)
items=len(deltas)
meanvalue=statistics.mean(deltas)
medianvalue=statistics.median(deltas)
stddevvalue=statistics.stdev(deltas)
stderrvalue=stddevvalue/math.sqrt(items)
print( "SUM OF ALL DELTAS: ",total)
print( "NUMBER OF DELTAS: ",items)
print( "MEAN: ",meanvalue)
print( "MEDIAN: ",medianvalue)
print( "STD ERR: ",stderrvalue)
print( "STD DEV: ",stddevvalue)
