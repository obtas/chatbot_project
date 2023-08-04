from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "AWS Helper",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        }
    ]
)
# chatbot.storage.drop()

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

trainer.train([
    "Can you help me?",
    "Sure, what would you like help with?"
])

trainer.train([
    "I would like some help",
    "Sure, what would you like help with?"
])

trainer.train([
    "Thanks for your help",
    "No problem, is there anything else you would like help with?",
    "No",
    "Thanks for chatting with me. Have a great day! 😊 "
])

trainer.train([
    "what is your name?",
    "My name is your AWS helper 😊 "
])

trainer.train("chat.txt")
trainer.train("chat_2.txt")
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english.greetings",
#               "chatterbot.corpus.english.conversations",
#               "chatterbot.corpus.english.botprofile")


# def chatbot():
# print("Type something to begin...")
# exit_conditions = (":q", "quit", "exit", "i'm done")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"😊 {chatbot.get_response(query)}")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # chatbot()
    return f"😊 {chatbot.get_response(userText)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)