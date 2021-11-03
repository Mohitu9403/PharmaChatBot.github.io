import random
print("BOT: What do you want me to call you?")
user_name = input()
bot_template = "BOT : {0}"
user_template = user_name + " : {0}"
name = "Funny Bot 101" 
weather = "rainy" 
mood = "Happy"
responses = { 
"what's your name?": [ 
"They call me {0}".format(name)]}