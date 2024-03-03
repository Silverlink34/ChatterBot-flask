from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import shutil

#code to copy database to mounted folder
shutil.copy("/app/db.sqlite3","/app/database/db.sqlite3")

chatbot = ChatBot("deepThought",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="/data/database.db",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ])

#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train(
#    "chatterbot.corpus.english"
#)

def talk(msg):
    return chatbot.get_response(msg)

def train(input,res):
    trainer = ListTrainer(chatbot)
    trainer.train([input,res])
    return "ok"
