import re
import os
from collections import Counter
import sys

words=list()
for file in os.listdir(sys.argv[1]):
  f=open(sys.argv[1]+file,'r')
  lines=f.readlines()
  for line in lines:
     for word in line.split(' '):
      newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')',''))))))).lower()
      if newword and newword != '-':
        words.append(newword)

counts=Counter(words)

len(counts)

i=0
for item in counts.most_common():
  if i==50: break
  print item
  i+=1
