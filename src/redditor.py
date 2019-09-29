class user:
    __init__(self, username, score):
        self.username = username
        self.score = score
    __str__(self):
        return username + ", " + str(score)
    