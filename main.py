#praw = Python Reddit API Wrapper
import praw
import random
import time

#create an instance of reddit, fill in the credentials according to your Reddit API registration and OAuth verification(For info on how to obtain your refresh token see PRAW documentation.)
reddit = praw.Reddit(client_id = '', 
                     client_secret = '', 
                     user_agent = '', 
                     redirect_uri = '', 
                     refresh_token = '', 
                     username = '', 
                     password = '')

#define what subreddit/s to search
sub = reddit.subreddit('')

#list of possible replies
replies = ['']

#define which posts to the subreddit to pull(remember to set a limit unless you want to pull all of reddit history)
for post in sub.rising(limit = 10):
    print(post.title)

    #loop through the comments on the post and search for a trigger phrase
    for comment in post.comments:
        if hasattr(comment, 'body'):
            comment_lower = comment.body.lower()
            #define the trigger phrase
            trigger = ''
            
            #if the trigger phrase was found, pull a random reply from replies list
            if trigger in comment_lower:
                random_index = random.randint(0, len(replies) - 1)
                
                #post a reply to the comment containing the trigger phrase using a random object from replies list
                comment.reply(replies[random_index])
                #sleep for a bit so you dont get banned for spam
                time.sleep(600)