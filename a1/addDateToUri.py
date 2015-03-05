import datetime
urislist=open('uniqueurinumbers','r')
uris=urislist.readlines()
uridates=list()
match=""
for uri in uris:
    print uri
    file="/home/jmcconne/cs751/a1/carbondate/"+uri[uri.rindex(' ')+1:].rstrip()+"/cd"
    carbondate=open(file,'r')
    cd=carbondate.readlines()
    for entry in cd:
        if entry.startswith('  "Estimated Creation Date"'):
            match=entry[entry.rindex(' ')+1:].replace('"','')[:10].rstrip()
            print match
    if match != "," and match != "":
      uridates.append(uri[:uri.rindex(' ')]+" "+match+"\n")
      match=""
    else:
      match=""
print uridates
uridatesfile=open('uniqueuridates','w+')
uridatesfile.writelines(uridates)
