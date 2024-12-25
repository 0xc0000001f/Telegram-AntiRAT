import requests

url = "https://api.telegram.org/bot47347923953725token/sendMessage"

payload = {
    "text": "useridfelanfilan\nWebsite: iploggerlink",
    "disable_web_page_preview": False,
    "disable_notification": False,
    "reply_to_message_id": 0,
    "chat_id": "logcuid"
}

headers = {
    "accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

