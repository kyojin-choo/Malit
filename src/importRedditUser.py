import praw
import configparser
#import pprint #pretty print
from collections import Counter
import malUser
import malComment
import sys

def cleanText (Text):
    # Cleaning text and lower casing all words
    for char in '-.,\n':
        Text=Text.replace(char,' ')
    Text = Text.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    return Text.split()

#take a list of names and return a dictonary
def main(userFile):
    config = configparser.ConfigParser()
    config.read("praw.ini")
    text_file = open(usernames, "r")
        
    #create a read only reddit instance
    #to authorize the reddit instance, add username and password to praw
    reddit = praw.Reddit(client_id = config["DEFAULT"]["id"], 
                         client_secret = config["DEFAULT"]["secret"], 
                         user_agent = config["DEFAULT"]["agent"])
    userInfo = []
    for name in usernames:
        try:
            user = reddit.redditor(name)
            prawcomment, count = findUserMaliciousComments(user, malList)
            comments = [];
            for c in prawcomments:
                comments.append(malComment(c.body, c.score, c.up, c.down))
            print(comments[0])
            userInfo.append(malUser(name, user.comment_karma, 
                                    malComment, count))
        except:
            console.log("possible 404 on name :" + name)
    return {name:findUserKeywordUsage(name) for name in usernames}


#given a PRAW redditor returns a list of PRAW comments containing mal words
def findUserMaliciousComments(user, profanityList):
    malComments = []
    count = 0
    for submission in user.comments.new(limit=1000):
        count += 1
        arr = cleanText(submission).split(" ")
        for word in arr:
            for profanity in profanityList:
                if word == profanity:
                    malComments.append(submission)
    return malComments, count
        

#takes a string username and finds that redditor
#returns a tuple list with the words they used and frequency
def findUserKeywordUsage(username):
    user = reddit.redditor(username)
    userComments = ""
    count = 0
    for submission in user.comments.new(limit=1000):#new(limit=5):
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


#print(main(["spez", "GallowBoob"]))
#print(user.link_karma) # to make it non-lazy
#pprint.pprint(vars(user))

#list of interesting attributes of our user:
#print("link karma: " + user.link_karma)
#print("comment karma: " + user.comment_karma)
#print(user._path)
    
#takes in a list of usernames
if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("NoNoNo")