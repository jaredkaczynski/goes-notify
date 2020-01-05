import requests

def send_notification(content, webhook):
    # if content == "test":
    #     print("Success")
    #     return
    payload = {
        "username": "Appointment Tracker",
        "content": content
    }
    response = requests.post(
        webhook,
        data=payload)
