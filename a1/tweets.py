# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
import subprocess
import os

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "2B9GeNZjvQvEpwFAulWvtXcrG"
CONSUMER_SECRET = "zAuo3ae8kY7TG7CS3eYLZVDiVXSem9Zccfvnt32YvmkQvcCeTJ"

#OAUTH_TOKEN = ""
#OAUTH_TOKEN_SECRET = ""

OAUTH_TOKEN= "2994069675-XUVam3bfRBCR0T9gdKd6a204eUiRGB44pnUSSUR"
OAUTH_TOKEN_SECRET= "ZECgm4Ee3GzlL10sy8eD7RG6ZIhvIdFNF8tU5PV9vRqB2"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print('Please go here and authorize: ' + authorize_url)
    
    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print( "OAUTH_TOKEN= \"" + token + "\"")
        print( "OAUTH_TOKEN_SECRET= \"" + secret +"\"")
        print()
    else:
        oauth = get_oauth()
        file=open('wordlist','r');
        uris=open('tweetsURI','a');
        words=file.readlines()
        linkcount=0
        badwords=['porn','nsfw','incest','penis','vagina','twitterafterdark','handjob','blowjob']

        for i in words:
          if linkcount >= 10000:
            break
          vurl="https://api.twitter.com/1.1/search/tweets.json?count=100&lang=en&q="+i
          print vurl
          r = requests.get(url=vurl, auth=oauth)
          alluris=json.loads(r.text)
          for uri in alluris.get("statuses"):
            skip=0
            for badword in badwords:
                if badword in str(uri):
                    skip=1
                    continue
            if len(uri.get("entities").get("urls")) > 0 and skip==0:
              fail=0
              for link in uri.get("entities").get("urls"):
                url=str(link.get("url"))
                print url
                urlend=url[url.rfind('/'):]
                uris.write("URLCOUNT:"+str(len(uri.get("entities").get("urls")))+"\n")
                uris.write("URL:"+url+"\n")
                uris.write("CREATED_AT:"+uri.get("created_at")+"\n")
                cmd="curl -I -L "+url
                try:
                  process=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                  headers,err=process.communicate()
                  uris.write("HEADERS:\n"+str(headers)+"\n")
                except:
                  uris.write("HEADERS:\nDELETED\n")
                  fail=1
                  continue
              if fail != 1:
                linkcount+=1
                uris.write("TWEET:\n"+json.dumps(uri)+"\n")
