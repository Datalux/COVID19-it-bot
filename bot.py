import requests

def sendImage(token, channel):
    files = {'photo': open('img.png', 'rb')}
    params = {'chat_id': channel}
    r= requests.post("https://api.telegram.org/bot" + token + '/sendPhoto', files=files, data=params)
    print(r.status_code, r.reason, r.content)

