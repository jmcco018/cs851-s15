import random
import os

file=open("uniqueurinumbers",'r')
lines=file.readlines()

alluris=list()
while True:
    if len(alluris) == 100:
      break
    rand=random.randint(0,len(lines))
    print rand
    try:
      size=os.path.getsize('/home/jmcconne/cs751/bodies/'+str(rand)+'/'+os.listdir('/home/jmcconne/cs751/bodies/'+str(rand))[0])
      if size > 20000:
        try:
          alluris.index(rand)
        except:
            os.mkdir('/home/jmcconne/cs751/a2/warcs/'+str(rand))
            os.mkdir('/home/jmcconne/cs751/a2/warcs/'+str(rand)+'/wget')
            os.mkdir('/home/jmcconne/cs751/a2/warcs/'+str(rand)+'/warcreate')
            os.mkdir('/home/jmcconne/cs751/a2/warcs/'+str(rand)+'/wail')
            os.mkdir('/home/jmcconne/cs751/a2/warcs/'+str(rand)+'/webrecorder')
            alluris.append(lines[rand])
    except:
      size=0

print alluris
output=open("uris","w+")
output.writelines(alluris)
