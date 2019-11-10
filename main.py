from flask import Flask, request, jsonify

from telegrambot import Telegram_Bot

from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)

Telegram_Bot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)    

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    bot = Telegram_Bot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success)  

if __name__ == "__main__":
    app.run(port=8443)