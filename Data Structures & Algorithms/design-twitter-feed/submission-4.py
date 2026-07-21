class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.tweet_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.posts[userId]) == 10:
            heapq.heappop(self.posts[userId])
        
        heapq.heappush(self.posts[userId],(self.tweet_time,tweetId))
        self.tweet_time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for i in self.following[userId]:
            for time,postid in self.posts[i]:
                heapq.heappush(h,(-time,postid))
        for time,postid in self.posts[userId]:
            heapq.heappush(h,(-time,postid))
        out = []
        for i in range(min(10,len(h))):
            out.append(heapq.heappop(h)[1])
        return out


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

