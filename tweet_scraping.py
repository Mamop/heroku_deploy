# -*- coding: utf-8 -*-


from requests_oauthlib import OAuth1Session
import json
from urllib import request


ck=os.environ["Consumer_key"]
cs=os.environ["Consumer_secret"]
at=os.environ["Access_token_key"]
as=os.environ["Access_token_secret"]

keys = {
        "CK":ck,
        "CS":cs,
        "AT":at,
        "AS":as,
        }
sess = OAuth1Session(keys["CK"],keys["CS"],keys["AT"],keys["AS"])

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
params = {"count":200,
          "exclude_entities" :1,
          "exclude_replies":1,
          }

req = sess.get(url, params = params)
timeline = json.loads(req.text)

f = open('markov_text.txt','w',encoding='CP932', errors='ignore')
lst = str.maketrans({
        '@':'',
        '#':''
        
        })

for tweet in timeline:
    f.write(tweet["text"].translate(lst).replace('https',''))
    
f.close()





            
            
        
        
