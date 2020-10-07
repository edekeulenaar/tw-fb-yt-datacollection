import requests, shutil,json,time, codecs, csv,sys
import pickle, os
from datetime import datetime

#Downloads data from YouTube. You may need to run this script several times as the API rate limit is limiting.

chans = ['YOUTUBE_ID_OF_CHANNEL_1', 'YOUTUBE_ID_OF_CHANNEL_2']
API_KEY = 'YOUR_API_KEY'


s=requests.Session()

video_id_list=[]
for phile in os.listdir('.'):
    if 'video_list_' in phile:
        video_id_list += pickle.load(open(phile, 'rb'))

cct=0
ct=0
if not os.path.isdir('comments'):
    os.makedirs('comments')


done=[]
try:
    done = pickle.load(open('videolist_dones_%s' % ("-".join(chans)),'rb'))
except Exceeded:
    pass

for vid in video_id_list:
    cct+=1
    ct+=1
    url = 'https://www.googleapis.com/youtube/v3/commentThreads?key=%s&textFormat=plainText&part=snippet&videoId=%s&maxResults=50' % (API_KEY, vid)
    pageToken=True
    zct=0
    while pageToken:
        zct+=1
        if not url:
            url = 'https://www.googleapis.com/youtube/v3/commentThreads?pageToken=%s&key=%s&textFormat=plainText&part=snippet&videoId=%s&maxResults=50' % (pageToken,API_KEY, vid)
        url_get = requests.get(url)
        res=None
        res = url_get.json()
        if 'dailyLimitExceeded' in str(res) or 'quotaExceeded' in str(res):
            sys.exit('Daily resource limit on the YouTube API exceeded, run this script again tomorrow to continue')
        ct+=1
        with open("comments/%s_%s.json"%(vid,zct), 'w') as f:
            json.dump(res,f)
        try:
            pageToken=res['nextPageToken']
        except KeyError:
            pageToken = None
        url = None
    print(vid, ct, cct, len(video_id_list))
    done.append(vid)
    pickle.dump(done, open('videolist_dones_%s' % ("-".join(chans)),'wb'))
    time.sleep(3)



