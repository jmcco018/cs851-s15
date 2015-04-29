from __future__ import division
import re
import os
from collections import Counter
import sys
import glob

f=open(sys.argv[1],'r')
files=f.readlines()

for folder in files:
    out=open("./"+folder.rstrip()+"/jaccard",'w')
    oldfile="./"+folder.rstrip()+"/0.boilerpipe"
    f=open(oldfile,'r')
    lines=f.readlines()

    oldwords=list()
    for line in lines:
     for word in re.split(' |>|<|\n|\t;',line):
      newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
      if newword and newword !=' ' and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
        oldwords.append(newword)

    for file1 in glob.glob('./'+folder.rstrip()+'/*.boilerpipe'):
        newfile="./"+file1.rstrip()
        f=open(newfile,'r')
        lines=f.readlines()
        words=list()
        for line in lines:
         for word in re.split(' |>|<|\n|\t;',line):
          newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
          if newword and newword !=' ' and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
            words.append(newword)
        
        if (words or oldwords):
          inter1=list(set(oldwords) & set(words));
          union1=list(set(words) | set(oldwords));
          jac1=1-abs(len(inter1))/abs(len(union1));
          print str('%.3f' % jac1)
          out.write(str('%.3f' % jac1)+'\n')
    out.close()
#print (oldthreewords);
#print (oldtwowords);

#print (threewords);
#print (twowords);
#counts=Counter(words)

#print len(counts.most_common())
