import praw
import configparser
import pprint #pretty print
from collections import Counter

def cleanText (Text):
    # Cleaning text and lower casing all words
    for char in '-.,\n':
        Text=Text.replace(char,' ')
    Text = Text.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    return Text.split()

#take a list of names and return a dictonary
def main(usernames):
    config = configparser.ConfigParser()
    config.read("praw.ini")
    maliciousList = ["reddit", "bomb"]    
        
    #create a read only reddit instance
    #to authorize the reddit instance, add username and password to praw
    reddit = praw.Reddit(client_id = config["DEFAULT"]["id"], 
                         client_secret = config["DEFAULT"]["secret"], 
                         user_agent = config["DEFAULT"]["agent"])
    return {name:findUserKeywordUsage(name) for name in usernames}

#takes a string username and finds that redditor
#returns a tuple list with the words they used and frequency
def findUserKeywordUsage(username):
    user = reddit.redditor(username)
    userComments = ""
    count = 0
    for submission in user.comments.top('all'):#new(limit=5):
        #print(submission.body)
        count += 1
        userComments += submission.body
        breakdown = Counter(cleanText(userComments)).most_common()
    
    maliciousTuples = []    
    for comment in breakdown:
        for word in maliciousList:
            if comment[0] == (word):
                maliciousTuples.append(comment)
    return maliciousTuples
                    
print(main(["spez", "GallowBoob"]))
#print(user.link_karma) # to make it non-lazy
#pprint.pprint(vars(user))

#list of interesting attributes of our user:
#print("link karma: " + user.link_karma)
#print("comment karma: " + user.comment_karma)
#print(user._path)