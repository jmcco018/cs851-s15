import re
import os
from collections import Counter
import sys


f=open(sys.argv[1],'r')
lines=f.readlines()

words=list()
for line in lines:
 for word in re.split(' |>|<|\n|\t;',line):
  newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
  if newword and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
    words.append(newword)


counts=Counter(words)

print len(counts.most_common())
