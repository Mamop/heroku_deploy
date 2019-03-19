# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:04:48 2019

@author: lenovo
"""

from requests_oauthlib import OAuth1Session
import json
from urllib import request


keys = {
        "CK":os.environ['Consumer_key'],
        "CS":os.environ['Consumer_secret'],
        "AT":os.environ['Access_token_key'],
        "AS":os.environ['Access_token_secret'],
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





            
            
        
        
