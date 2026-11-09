from collections import defaultdict
import heapq as hq
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.time_stamp = 0
        self.post = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append((self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        for time_stamp, tweetId in self.post[userId]:
            hq.heappush(min_heap, (time_stamp,tweetId))
            if len(min_heap) > 10:
                hq.heappop(min_heap)
        for followeeId in self.following[userId]:
            for time_stamp, tweetId in self.post[followeeId]:
                hq.heappush(min_heap, (time_stamp,tweetId))
                if len(min_heap) > 10:
                    hq.heappop(min_heap)
        res = []
        while min_heap:
            time_stamp, tweetId = hq.heappop(min_heap)
            res.append(tweetId)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
