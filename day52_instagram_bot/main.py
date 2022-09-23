from instagram_follower import InstaFollower

instagram_follower = InstaFollower()
instagram_follower.login()
followers = instagram_follower.find_followers()
instagram_follower.follow(followers)

