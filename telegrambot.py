import requests
import re
import json

from config import TELEGRAM_SEND_MESSAGE_URL

class Telegram_Bot:
    
    def __init__(self):
        """"
        Initializes an instance of the TelegramBot class.
        Attributes:
            chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
            text:str: Text of Telegram chat
            first_name:str: First name of the user who sent the message
            last_name:str: Last name of the user who sent the message
        """

        self.chat_id = None
        self.text = None

        self.symbol = None
        self.trade = None
        self.entry = None
        self.stoploss = None
        self.takeprofit1 = None
        self.takeprofit2 = None


    def parse_webhook_data(self, data):
        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions

        Args:
            data:str: JSON string of data
        """

        message = data['message']

        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        self.first_name = message['from']['first_name']
        self.last_name = message['from']['last_name']




    def action(self):
        """
        Conditional actions based on set webhook data.
        Returns:
            bool: True if the action was completed successfully else false
        """
        symbols = ['USDCHF','GBPUSD','EURUSD','USDJPY','USDCAD','AUDUSD','EURGBP','EURAUD','EURCHF','EURJPY','BGPCHF','CADJPY','GBPJPY','AUDNZD','AUDCAD','AUDCHF','AUDJPY','CHFJPY','EURNZD','EURCAD','CADCHF','NZDJPY','NZDUSD','GBPNZD','XAUUSD']
        lowersymbols = [x.lower() for x in symbols]
        signals = ['buy','sell']
        strEntry = "entry"
        strSL = "sl"
        strTP = "tp"
        regexDigits = '[0-9]+.[0-9]+'

        symbol = None
        signal = None
        entry = None
        SL = None
        TP = None

        success = None

        # incoming message is split
        messagesplit = json.dumps(self.incoming_message_text.split())
        print(messagesplit)


        # Check for symbol
        for x in lowersymbols:
            if x in messagesplit:
                symbol = x
                # Check for trade signal
                if symbol != False:
                    for i in signals:
                        if i in messagesplit:
                            signal = i
                            


                


#self.outgoing_message_text = "Symbol found! {}".format(x)
#success = self.send_message()


        if self.incoming_message_text == 'test':
            self.outgoing_message_text = 'Successful test 🙌'
            success = self.send_message()

        return success


    def send_message(self):
        """
        Sends message to Telegram servers.
        """

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

        return True if res.status_code == 200 else False


    @staticmethod
    def init_webhook(url):
        """
        Initializes the webhook
        Args:
            url:str: Provides the telegram server with a endpoint for webhook data
        """

        requests.get(url)    