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
print( "MEAN OF ALL DELTAS: ",meanvalue)
print( "MEDIAN OF ALL DELTAS: ",medianvalue)
print( "STD ERR OF ALL DELTAS: ",stderrvalue)
print( "STD DEV OF ALL DELTAS: ",stddevvalue)
