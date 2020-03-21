import requests

def sendImage(token, channel, contagi, tamponi):
    files = {'photo': open('img.png', 'rb')}
    cap = "CONTAGI: " + str(contagi) + "\nTAMPONI EFFETTUATI: " + str(tamponi) 
    params = {'chat_id': channel, 'caption': cap}
    r= requests.post("https://api.telegram.org/bot" + token + '/sendPhoto', files=files, data=params)
    print(r.status_code, r.reason, r.content)

