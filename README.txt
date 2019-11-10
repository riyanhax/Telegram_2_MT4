# Telegrambot to MT4 
### Using Telegram, Ngrok, MetaTrader 4

1. Run main.py
2. A local server will be initialized as well as an ngrok local host.
3. Connect your telegram bot to the server using your Telegram Bot Token in the Telegram_Token part of config.py file 
4. The local server does all the processing, using flask to open the doors and send it to the local url. Ngrok uses the same port, 
   takes the local url and transforms it to external, allowing the transfer of data to Telegram and reception also.