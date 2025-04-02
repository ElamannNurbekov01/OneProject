import requests

API_TOKEN = "8146265649:AAENJSO1LvzXcJd0jKlWUGG39SC5GflfQxg"
CHAT_ID = "-1002546050589"
API = "https://api.telegram.org/bot"
method = API + API_TOKEN + '/sendMessage'

def send_group_message():
    requests.post(
        method, data={
            'chat_id': CHAT_ID,
            "text": "Вы создали машину"
        }
    )

def Changing_machines():
    requests.post(
        method, data={
            'chat_id': CHAT_ID,
            "text": "Вы изменили характеристики машины"
        }
    )

def Car_deleted():
    requests.post(
        method, data={
            'chat_id': CHAT_ID,
            "text": "Вы удалили машину"
        }
    )



