With API changes pushed by "New Twitter" this script no longer works. 

# Unliked

This program is a further modification of melissa mcewen's modification of Quincy Larson's tweet deletion Python script. This is a Python 2 script that imports a modified like.js (named like2.js) that contains one Tweet ID per line and nothing else. It should be noted that I've found conflicting information about Twitter's rate limiting, as some say the 15 per 15 minutes holds true, others say it could be more. I took the cautious approach and did the following workflow:

1. Attempt to like Tweet
2. Wait 30 seconds
3. Attempt to unlike Tweet.
4. Wait 30 seconds.
5. If there's an error, try to unlike the tweet again.
6. Wait 30 seconds.

This, in an ideal environment, has the potential to unlike 1440 tweets per day. It's SLOW. On purpose.
Sources:
https://medium.com/@melissamcewen/how-to-completely-delete-your-twitter-likes-5a41c35aefb8

https://gist.github.com/melissamcewen/37125ee31615f3f7f53de47459053bf1#file-unlike-py

https://medium.freecodecamp.org/how-to-delete-your-past-tweets-in-bulk-and-for-free-save-yourself-from-your-past-self-f8844cdbda2

https://github.com/QuincyLarson/delete-tweets
