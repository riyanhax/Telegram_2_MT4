from pyngrok import ngrok

Ngrok_URL = ''

Ngrok_URL = ngrok.connect(port=8443,proto="http")
Ngrok_URL = Ngrok_URL.replace('http','https')
Ngrok_URL = Ngrok_URL
Local_Ngrok_Webhook_Endpoint = '{}/webhook'.format(Ngrok_URL)


# telegram bot url
Telegram_Token = '776136455:AAHPu2Wp5npo8rMvrBp0KSmLXagImYr9Qf8'
Base_Telegram_URL = 'https://api.telegram.org/bot{}'.format(Telegram_Token)
    

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(Base_Telegram_URL, Local_Ngrok_Webhook_Endpoint)
TELEGRAM_SEND_MESSAGE_URL = Base_Telegram_URL + '/sendMessage?chat_id={}&text={}'

print(TELEGRAM_INIT_WEBHOOK_URL)