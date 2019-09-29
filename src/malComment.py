class malComment:
    def __init__(self, text, upvote, downvote, karma):
        self.commentText = text
        self.upvotes = upvote
        self.downvotes = downvote
        self.karma = karma
    def __repr__(self):
        return ""#self.commentText + str(self.upvotes) + str(self.downvotes) + str(self.karma)
    def __str__(self):
        return ""#self.commentText + str(self.upvotes) + str(self.downvotes) + str(self.karma)