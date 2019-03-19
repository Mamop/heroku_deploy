# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:49:51 2019

@author: lenovo
"""


import random
from janome.tokenizer import Tokenizer
from requests_oauthlib import OAuth1Session

def wakati(text):
    text = text.replace('\n','')
    text = text.replace('\r','')
    t = Tokenizer()
    result = t.tokenize(text, wakati=True)
    return result

def generate_text(num_sentence=1):
    filename = "markov_text.txt"
    src = open(filename,"r").read()
    wordlist = wakati(src)
    
    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1,w2) not in markov:
                markov[(w1,w2)] = []
            markov[(w1,w2)].append(word)
        w1, w2 = w2,word
    
    count_kuten = 0
    num_sentence = num_sentence
    sentence = ""
    w1,w2 = random.choice(list(markov.keys()))
    while count_kuten < num_sentence:
        tmp = random.choice(markov[(w1,w2)])
        sentence += tmp
        if(tmp=='。' or tmp=='！' or tmp=='？'):
            count_kuten += 1
            sentence += '\n'
        w1,w2 = w2,tmp
    
    ck=os.environ["Consumer_key"]
    cs=os.environ["Consumer_secret"]
    at=os.environ["Access_token_key"]
    as=os.environ["Access_token_secret"]
    
    keys ={
            "CK":ck,
            "CS":cs,
            "AT":at,
            "AS":as,}
    
    sess=OAuth1Session(keys["CK"], keys["CS"], keys["AT"], keys["AS"])
    
    url ="https://api.twitter.com/1.1/statuses/update.json"   
    params={"status":sentence[:random.randint(60,90)]}
    
    req=sess.post(url, params = params)
    
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error")
    
    
if __name__ == "__main__":
    generate_text()
    
