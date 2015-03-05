import datetime
import time

urislist=open('../uniqueuridates','r')
uridates=urislist.readlines()

tweets=open('../tweetsURI','r')
lines=tweets.readlines()
link=""
tweettime=""
urltime=""
timedifs=list()

for line in lines:
    if line.startswith("CREATED_AT:"):
        time=line[line.index(' ')+1:][:6]+line[line.rindex(' '):].rstrip()
        tweettime=datetime.datetime.strptime(time,"%b %d %Y").strftime('%Y-%m-%d')
        continue
    elif line.lower().startswith("location:"):
        link=line[10:].rstrip()
        continue
    elif line.startswith("URL:"):
        link=line[4:].rstrip()
        continue
    elif line.startswith("URLCOUNT:") or line.startswith("TWEET:"):
        if link != "" and tweettime !="":
            match=[s for s in uridates if link in s]
            if len(match) > 0:
                urltime=match[0][match[0].rindex(' ')+1:]
                timedifs.append(str(abs((datetime.datetime.strptime(tweettime.rstrip(),"%Y-%m-%d") -  datetime.datetime.strptime(urltime.rstrip(),"%Y-%m-%d")).days))+"\n")
            else:
                timedifs.append("0\n")
            link=""
            tweettime=""
            urltime=""
            match=""
    else:
        continue
file=open('timedif','w+')
file.writelines(timedifs)
