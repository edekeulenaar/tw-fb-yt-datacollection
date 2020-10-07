# tw-fb-yt-datacollection
Code to collect tweets, Facebook posts and YouTube comments that mention words from a pre-determined lexicon. 

First: edit dictionary.csv to list the terms you're looking for, plus if you like agenda's and discourses. There's a separate column for Twitter in case the terms used there are different from the other platforms.

***FACEBOOK***

You'll need a page token for the Facebook page, plus enough permissions in the Facebook API to read the comments on that page.

Edit get_facebook_data.py and set the page token.

Run:
> python get_facebook_data.py
OR
> python3 get_facebook_data.py
(whichever works).


This will create a file called 'facebook_comments.csv' with all the comments in it, as well as a file called 'fb_posts.csv' that lists all the posts the comments were made to.



***YOUTUBE***

You'll need an API key for YouTube. Edit get_youtube_data.py as well as get_youtube_comments.py and set the token.

Edit get_youtube_data.py and set the channel(s) you want to include, and the date of the oldest video you're willing to include.

First run:
> python get_youtube_data.py
OR
> python3 get_youtube_data.py
(whichever works).

This will download the video IDs from the selected channels.

Edit get_youtube_comments.py and set the channel(s) you want to include as well as the API key.

Then run:
> python get_youtube_comments.py
OR
> python3 get_youtube_comments.py
(whichever works).

This will dump the comments to the 'comments' directory. Note that you may not have enough credits to download everything at once - if your rate limit is exceeded, wait a day and run the script again.

Then run
> python filter_youtube_data.py
OR
> python3 filter_youtube_data.py
(whichever works).

This will make a file called 'youtube_comments.csv', listing all of the comments.



***TWITTER***

Get API credentials and enter them into get_twitter.py.

Then run
> python get_twitter.py
OR
> python3 get_twitter.py
(whichever works).

This will dump a list of tweets into the directory called 'tweets', including the current date in the filename, one file per search term.
You can run this multiple times to gather data over time - the final join will remove any duplicate tweets.