tweets=open('tweetsURI','r')
lines=tweets.readlines()
uniquris=list()
alluris=list()
dupuris=list()
link=""
for line in lines:
    if line.lower().startswith("location:"):
        link=line[9:]
        continue
    if line.startswith("URL:"):
        link=line[4:]
        continue
    elif line.startswith("URLCOUNT:") or line.startswith("TWEET:"):
        if link != "":
            try:
                uniquris.index(link)
                try:
                    dupuris.index(link)
                except:
                    dupuris.append(link)
            except:
                uniquris.append(link)
            alluris.append(link)
            link=""
            continue
    else:
        continue
print "All URIs: "+str(len(alluris))
print "Duplicate URIs: "+str(len(dupuris))
print "Unique URIs: "+str(len(uniquris))

finaluri=open('uniqueuri','w+')
finaluri.writelines(uniquris)
dupuri=open('dupuri','w+')
dupuri.writelines(dupuris)
