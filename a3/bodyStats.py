import re
import os
from collections import Counter
import sys


f=open(sys.argv[1],'r')
files=f.readlines()

words=list()
for file in files:
  print file.rstrip()
  f=open(file.rstrip(),'r')
  lines=f.readlines()
  for line in lines:
     for word in re.split(' |>|<|\n|\t;',line):
      newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
      if newword and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
        words.append(newword)

counts=Counter(words)

len(counts)

i=0
for item in counts.most_common():
  if i==100: break
  print item
  i+=1
