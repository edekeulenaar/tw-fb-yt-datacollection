import os,codecs,csv,twarc, pickle,json
from datetime import datetime

#Gets current tweets for terms in the dictionary

consumer_key='YOUR_CONSUMER_KEY'
consumer_secret='YOUR_CONSUMER_SECRET_KEY'
access_token='YOUR_ACCESS_TOKEN'
access_token_secret='YOUR_ACCESS_TOKEN_SECRET'


Tt = twarc.Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

wanted_terms = []
termdic={}
with codecs.open('dictionary.csv','r', encoding='utf-8') as f:
    r=csv.DictReader(f, delimiter=';')
    for row in r:
        wanted_terms.append(row['twitter_term'])


if not os.path.isdir('tweets'):
    os.makedirs('tweets')

now=datetime.datetime.now()


tweets=[]
for term in wanted_terms:
    print(term)
    for i, tweet in enumerate(Tt.search(wanted_terms)):
        tweets.append(tweet)
        if i % 100 == True:
            print(term,i)
        with codecs.open('tweets/%s_%s.jsonl' % (term, str(now), 'w', encoding='utf-8') as f:
            for t in tweets:
                json.dump(t, f)
                f.write("\n")
