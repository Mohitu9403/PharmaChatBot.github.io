#imports
from flask import Flask, render_template
import random
'''print("Chat_bot: What should I call you?")'''
user_input = input()
chatbot_temp = "BOT : {}"
user_temp = user_input + " : {}"
Chatbot_name = "Chatbot" 
temperature = "cold" 
mood = "Happy"
work = "Guide"
domains= "Finance, Marketing, IT, Real-estate, HR, Operations "
app = Flask(__name__, template_folder="template")
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()



print("Chat_bot: What should I call you?")
user_input = input()
chatbot_temp = "BOT : {}"
user_temp = user_input + " : {}"
Chatbot_name = "Chatbot" 
temperature = "cold" 
mood = "Happy"
work = "Guide"
domains= "Finance, Marketing, IT, Real-estate, HR, Operations "

Output = { 
"what's your name?": [ 
"I am {}".format(Chatbot_name), ],
"what's today's temperature?": [ 
"Its {}".format(temperature),  ],
"how are you?": [ 
"I am feeling {}".format(mood), 
"{}! And you?".format(mood), ],
"In what domains do you guide?": [
"I give consultation in {}".format(domains)],
"what is your work?": [ 
"I am  {}".format(work), 
"I feel good to  {}".format(work), 
"I am called business {}".format(work) ],
"default": [
"this is a default message"] }
@app.route("/get")
def reply(message):
    if message in Output: 
        bot_message = random.choice(Output[message])
    else: 
        bot_message = random.choice(Output["default"])
    return bot_message

def reply(message):
    if message in Output: 
        bot_message = random.choice(Output[message])
    else: 
        bot_message = random.choice(Output["default"])
    return bot_message
if __name__ == "__main__":
    app.run()


def key_words(key): 
  if "name" in key: 
    value = "what's your name?"
  elif "temperature" in key:  
     value = "what's today's temperature?"
  elif "robot" in key: 
     value = "are you a robot?"
  elif "how are" in key: 
     value = "how are you?"
  elif "work" in key: 
          value  = "what is your work?"
  elif "domains" in key: 
          value = "In what domains do you guide?"
  else: 
     value = ""
  return value
def send_message(message): 
  print(user_temp.format(message)) 
  response = reply(message) 
  print(chatbot_temp.format(response))

while 1: 
  my_input = input() 
  my_input = my_input.lower() 
  related_text = key_words(my_input) 
  send_message(related_text)
  if my_input == "exit": 
   break

if __name__ == "__main__":
    app.run()

