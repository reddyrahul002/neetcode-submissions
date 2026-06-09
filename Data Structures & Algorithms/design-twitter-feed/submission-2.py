import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)        
        self.following = defaultdict(set) 
        self.time=0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap=[]
        users = self.following[userId] | {userId} 
        for user in users:
            for tweet in self.tweets[user]:
                heap.append(tweet) 
        
        top=heapq.nlargest(10,heap)
        return [i[1] for i in top]



        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
