class malUser:
    def __init__(self, name, commentKarma, comments, age, numComment, wordCount):
        self.name = name
        self.karma = commentKarma
        self.comments = comments
        self.age = age
        self.numComment = numComment
        self.wordCount = wordCount
    def __repr__(self):
        return self.name + str(self.karma) + str(self.age) + str(self.numComment) + "/n".join([str(c) for c in self.comments])
    def __str__(self):
        return self.name + str(self.karma) + str(self.age) + str(self.numComment) + "/n".join([str(c) for c in self.comments])
