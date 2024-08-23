import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23854583"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3f073dbb45a1cb3a817e5743ad139d2e")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mithleshchauhan3679:M18upE8eNZrr2QH9@cluster1.wymiz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
