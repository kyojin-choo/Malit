import praw
import configparser
#import pprint #pretty print
from collections import Counter
import malUser
import malComment
from profanity import badwords as pf
import sys
import time

def cleanText (Text):
    # Cleaning text and lower casing all words
    for char in '-.,\n':
        Text=Text.replace(char,' ')
    Text = Text.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    return Text.split()

#take a list of names and return a list of objects
def main():
    file = open("sampleData.txt", "r")
    lines = file.read().split("\" \"")
    usernames = list(dict.fromkeys(lines))
    config = configparser.ConfigParser()
    config.read("praw.ini")
        
    #create a read only reddit instance
    #to authorize the reddit instance, add username and password to praw
    reddit = praw.Reddit(client_id = config["DEFAULT"]["id"], 
                         client_secret = config["DEFAULT"]["secret"], 
                         user_agent = config["DEFAULT"]["agent"])
    userInfo = []
    keys = pf()

    for name in usernames:
#        try:
        user = reddit.redditor(name)
        prawcomments, count, wordCount, age = findUserMaliciousComments(user, list(keys))
        comments = [];
        for c in prawcomments:
            a = malComment.malComment(c.body, c.score, c.ups, c.downs)
            comments.append(a)
        userInfo.append(malUser.malUser(name, user.comment_karma, 
                                        comments, time.time() - age, count, wordCount))
 #       except:
  #          print("possible 404 on name :" + name)
    return userInfo


#given a PRAW redditor returns a list of PRAW comments containing mal words
def findUserMaliciousComments(user, profanityList):
    malComments = []
    count = 0
    wordCount = 0
    for submission in user.comments.new(limit=100):
        count += 1
        #print(cleanText(submission.body))
        arr = cleanText(submission.body)
        for word in arr:
            wordCount += 1
            for profanity in profanityList:
                if word == profanity:
                    malComments.append(submission)
        age = submission.created
        
    return malComments, count, wordCount, age
        

#takes a string username and finds that redditor
#returns a tuple list with the words they used and frequency
def findUserKeywordUsage(user):
    userComments = ""
    count = 0
    for submission in user.comments.new(limit=1000):
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
    
