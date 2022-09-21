from internet_speed_bot import InternetSpeedBot
from twitter_bot import TwitterBot

internet_bot = InternetSpeedBot()
internet_speed = internet_bot.get_internet_speed()
print(internet_speed)

twitter_bot = TwitterBot()
# twitter_bot.say_hello()
if internet_bot.check_up_speed() and internet_bot.check_down_speed():
    message = f"Greate speeds by internet provider with {str(internet_speed[0])} down and {str(internet_speed[1])} up!"
elif internet_bot.check_down_speed():
    message = f"Good down speed by internet provider at {str(internet_speed[0])}."
elif internet_bot.check_up_speed():
    message = f"Good up speed by internet provider at {str(internet_speed[1])}."
else:
    message = f"Internet provider not meeting expected speeds with {str(internet_speed[0])} " \
              f"down and {str(internet_speed[1])} up."
twitter_bot.send_tweet(message=message)
