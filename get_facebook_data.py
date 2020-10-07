from facebook import GraphAPI
import pickle, requests, time
from facebook_scraper import get_posts

#Downloads comments from a Facebook page

#Note you need to be authorized properly to access the posts
page_token='YOUR_PAGE_TOKEN_HERE'

ct=0

#Download all the posts from the relevant page
postlist=[]
for post in get_posts('FACEBOOK_PAGE_NAME', pages=1000, extra_info=True):
    ct+=1
    postlist.append(post)
    if ct % 10 == True:#Periodically save the information
        pickle.dump(postlist, open('fb_posts.p','wb'))

#Final save
pickle.dump(postlist, open('fb_posts.p','wb'))


#To start getting comments, instantiate the graph API
graph = GraphAPI(page_token)

#Save the posts to a .csv, so they are readable
csvdata=[]
post_ids=[]
keys=[]
for post in postlist:
    csvdata.append(post)
    keys += list(post.keys())
    post_ids.append(post['id'])
keys=list(set(keys))
with codecs.open('fb_posts.csv','w', encoding='utf-8') as f:
    w=csv.DictWriter(f, delimiter=';', fieldnames=list(keys))
    w.writeheader()
    w.writerows(csvdata)


#Get all the comments
gatherer = {}
for i, post_id in enumerate(post_ids):
    try:
        gatherer[post]
    except KeyError:
        print(post_id, i, len(ids))
        time.sleep(5)
        comments = []
        post_comments = graph.get_connections(id=post_id, connection_name="comments")
        comments.extend(post_comments["data"])
        while True:
            try:
                post_comments =  requests.get(post_comments["paging"]["next"]).json()
                comments.extend(post_comments["data"])
            except KeyError:
                break
        gatherer[post_id]=comments
        #save it
        pickle.dump(gatherer, open('fbcomments.p','wb'))


#Save it as a .csv
out=[]
keys = []
for post_id, list_of_posts in gatherer.items():
    for fb_post in list_of_posts:
        #Set the ID of the post in the post itself
        fb_post['post_id'] = post_id
        keys += list(fb_post.keys())
        out.append(fb_post)

keys=list(set(keys))

with codecs.open('fb_comments.csv','w', encoding='utf-8') as f:
    w=csv.DictWriter(f, delimiter=';', fieldnames=keys)
    w.writeheader()
    w.writerows(out)
