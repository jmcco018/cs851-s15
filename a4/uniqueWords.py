from __future__ import division
import re
import os
from collections import Counter
import sys


f=open(sys.argv[1],'r')
files=f.readlines()
for file1 in files:
    oldfile="../bodyFiles/"+file1.rstrip()
    newfile="../bodyFilesNew/"+file1.rstrip()
    f=open(newfile,'r')
    lines=f.readlines()

    words=list()
    twowords=list()
    threewords=list()
    prevword="";
    prev2word="";
    oneword="";
    for line in lines:
     for word in re.split(' |>|<|\n|\t;',line):
      newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
      if newword and newword !=' ' and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
        words.append(newword)
        prev2word = prevword;
        prevword = oneword;
        oneword = newword;
        if prevword and prev2word:
          twoword = prevword+' '+newword;
          threeword = prev2word+' '+prevword+' '+newword;
          twowords.append(twoword);
          threewords.append(threeword);
    
    f=open(oldfile,'r')
    lines=f.readlines()

    oldwords=list()
    oldtwowords=list()
    oldthreewords=list()
    prevword="";
    prev2word="";
    oneword="";
    for line in lines:
     for word in re.split(' |>|<|\n|\t;',line):
      newword=re.sub(':$','',re.sub('\?$','',re.sub(",$",'',re.sub('!$','',re.sub('^/','',re.sub('/$','',re.sub('\.$','',re.sub('\n$','',word.replace('(','').replace(')','').replace('/\t',''))))))))).lower()
      if newword and newword !=' ' and newword != '-' and newword !='--' and newword !='!--' and newword!='+' and newword!='};' and newword !='"' and newword !='}' and newword !='{' and "\t" not in newword:
        oldwords.append(newword)
        prev2word = prevword;
        prevword = oneword;
        oneword = newword;
        if prevword and prev2word:
          twoword = prevword+' '+newword;
          threeword = prev2word+' '+prevword+' '+newword;
          oldtwowords.append(twoword);
          oldthreewords.append(threeword);
    if (words or oldwords) and (twowords or oldtwowords) and (threewords or oldthreewords):
      inter1=list(set(oldwords) & set(words));
      inter2=list(set(oldtwowords) & set(twowords));
      inter3=list(set(oldthreewords) & set(threewords));
      union1=list(set(words) | set(oldwords));
      union2=list(set(twowords) | set(oldtwowords));
      union3=list(set(threewords) | set(oldthreewords));
      jac1=1-abs(len(inter1))/abs(len(union1));
      jac2=1-abs(len(inter2))/abs(len(union2));
      jac3=1-abs(len(inter3))/abs(len(union3));
      print str('%.3f' % jac1)+','+str('%.3f' % jac2)+','+str('%.3f' % jac3)

#print (oldthreewords);
#print (oldtwowords);

#print (threewords);
#print (twowords);
#counts=Counter(words)

#print len(counts.most_common())
