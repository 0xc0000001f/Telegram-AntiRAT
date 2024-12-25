import requests

url = "https://api.telegram.org/bot47347923953725tokenfelanfilan/sendDocument"

payload = {
    "document": "pdfdosyasi",
    "caption": "message", # use \n
    "disable_notification": False,
    "reply_to_message_id": 0,
    "chat_id": "loggerid"
}

headers = {
    "accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
