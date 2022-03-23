import requests

myToken = "xoxb-my-token"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

    print(response)

post_message(myToken,"#bitcoin","whee-coin-test")