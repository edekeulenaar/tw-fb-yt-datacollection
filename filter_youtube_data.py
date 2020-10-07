import codecs, csv, re, json, os

#Filters YT comments by terms in dictionary.csv and outputs a new csv with only comments mentioning the wanted terms


wanted_terms = []
termdic={}
with codecs.open('dictionary.csv','r', encoding='utf-8') as f:
    r=csv.DictReader(f, delimiter=';')
    for row in r:
        wanted_terms.append(row['term'])
        termdic[term] = [row['agenda'], row['discourse']

columns=['platform','day-month-year-hour','post containing anti-un term','agenda','anti-un term','original un fb, yt or tw post','username (wanted_termstag value)','user category (authentic/inauthentic)','mentions','retweets','likes/loves','account still up?']

out=[]
for x in os.listdir('../comments'):
    vid=x[:11]
    dta = json.load(open('../comments/%s'%x,'r'))
    print(dta.keys())
    if 'items' in dta.keys():
        for itm in dta['items']:
            itm=itm['snippet']
            itm=itm['topLevelComment']
            itm=itm['snippet']
            txt=itm['textOriginal']
            founds=[]
            for term in wanted_terms:
                test = re.search(r'\b%s\b' % term.lower(), txt.lower())
                if test:
                    founds.append(term)
            if len(founds)>0:
                dic={}
                for z in columns:
                    dic[z] = None
                dic['platform'] = 'Youtube'
                dic['day-month-year-hour'] = itm['publishedAt']
                dic['post containing anti-un term'] = txt
                dic['anti-un term'] = ','.join(founds)
                dic['agenda'] = []
                for ff in founds:
                    dic['agenda'].append(termdic[ff][0])
                dic['agenda'] = ','.join(dic['agenda'])
                dic['discourse'] = []
                for ff in founds:
                    dic['discourse'].append(termdic[ff][1])
                dic['discourse'] = ','.join(dic['discourse'])
                dic['likes/loves'] = itm['likeCount']
                out.append(dic)

with codecs.open('youtube_comments.csv','w', encoding='utf-8') as f:
    w=csv.DictWriter(f, delimiter=';', fieldnames=columns)
    w.writeheader()
    w.writerows(out)