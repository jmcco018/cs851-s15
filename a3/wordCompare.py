import re
import os
from collections import Counter
import sys

words=list()
f=open(sys.argv[1],'r')
lines=f.readlines()
for line in lines:
  words.append(re.sub("'.*",'',re.sub("^\('",'',line)).rstrip())
print words

stopwords=list()
f=open(sys.argv[2],'r')
lines=f.readlines()
for line in lines:
  stopwords.append(line.rstrip())
print stopwords

for word in stopwords:
    try:
      words.remove(word)
    except:
      continue
print words
