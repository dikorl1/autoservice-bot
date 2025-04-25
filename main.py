import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import openai

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

openai.api_key = OPENAI_API_KEY

def handle_message(update, context):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_text}]
    )
    reply_text = response.choices[0].message["content"]
    update.message.reply_text(reply_text)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    app.run(port=5000)
