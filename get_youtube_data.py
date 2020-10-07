import requests, shutil,json,time, codecs, csv,sys
import pickle, os
from datetime import datetime

#Downloads data from YouTube. You may need to run this script several times as the API rate limit is limiting.

chans = ['YOUTUBE_ID_OF_CHANNEL_1', 'YOUTUBE_ID_OF_CHANNEL_2']
API_KEY = 'YOUR_API_KEY'
FROM_DATE = '2019-11-01' #the date of the oldest videos to include


s=requests.Session()

    
for chan in chans:
    if not chan.strip() or os.path.isfile('vidlist/%s.p'% chan):
        continue
    url = 'https://www.googleapis.com/youtube/v3/search?key=' + API_KEY +'&channelId=' + chan + '&part=snippet,id&order=date&maxResults=50'
    print(chan)
    first = datetime.strptime(FROM_DATE, "%Y-%m-%d")
    ok=True
    dats=[]
    vidlist=[]
    while ok:
        try:
            res = s.get(url)
            res = json.loads(res.text)
            try:
                er = res['error']
                print(er)
                sys.exit('Something went wrong')
            except KeyError:
                pass
            try:
                NextPageToken = res['nextPageToken']
            except KeyError:
                NextPageToken = None
                ok=False
            
            for itm in res['items']:
                dt = datetime.strptime(itm['snippet']['publishedAt'][:10], "%Y-%m-%d")
                try:
                    vid=itm['id']['videoId']
                    if dt < first:#video too old
                        ok=False
                    else:
                        vidlist.append(vid)
                except KeyError:
                    pass
            if ok:
                url = 'https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId=' + chan + '&part=snippet,id&order=date&maxResults=50&pageToken='+NextPageToken
            dats.append(res)
        except Exception as err:
            print(err)
            ok=False
    pickle.dump(vidlist, open('video_list_%s.p'% chan,'wb'))
    pickle.dump(dats, open('channeldata_%s.p'% chan,'wb'))

