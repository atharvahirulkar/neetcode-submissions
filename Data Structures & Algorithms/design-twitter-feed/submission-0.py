from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      
        self.following = defaultdict(set)    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.following[userId].add(userId)

    
        for followee in self.following[userId]:
            if followee in self.tweets:
                idx = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

    
        while heap and len(res) < 10:
            time, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)