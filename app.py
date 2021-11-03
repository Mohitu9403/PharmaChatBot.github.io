# Imports 

from typing import List 
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Training Example')
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
    "Satyajit",
    "khot",
])

trainer.train([
    "Greetings!",
    "Hello",
])

app = Flask(__name__, template_folder="template")
#create chatbot
#trainer = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(englishBot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")


#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()