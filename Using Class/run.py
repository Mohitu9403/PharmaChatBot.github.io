import random
print("Chat_bot: What's your name?")
user_input = input()
chatbot_temp = "BOT - {}"
user_temp = user_input + " - {}"
Chatbot_name = "Chatbot" 
work = "Guide"
domains= "Finance, Marketing, IT, Real-estate, HR, Operations "

Output = { 
"what's your name?": [ 
"My nickname is {}".format(Chatbot_name), 
"I feel good calling me {}".format(Chatbot_name), 
"My name is the {}".format(Chatbot_name) ],
"In what domains do you guide?": [
"I give consultation in {}".format(domains)],
"what is your work?": [ 
"I am  {}".format(work), 
"I feel good to  {}".format(work), 
"I am called business {}".format(work) ],
"default": [
"default message"] }

def reply(message):
    if message in Output: 
        bot_message = random.choice(Output[message])
    else: 
        bot_message = random.choice(Output["default"])
    return bot_message

def key_words(key): 
    if "name" in key: 
         value = "what's your name?"
    elif "work" in key: 
         value = "what is your work?"
    elif "domains" in key: 
         value = "In what domains do you guide?"
    else: 
         value = ""
    return value
    
def send_message(message): 
    print(user_temp.format(message)) 
    response = Output(message) 
    print(chatbot_temp.format(response))

while 1: 
  my_input = input() 
  my_input = my_input.lower() 
  related_text = key_words(my_input) 
  send_message(related_text)
  if my_input == "exit": 
   break

