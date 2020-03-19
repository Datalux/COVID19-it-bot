import Setup
import bot
import schedule, time
import pylab
import urllib.request, json 
import os
import matplotlib.pyplot as plt
import matplotlib

setup = Setup.Setup()
stime = setup.get_time()
token = setup.get_token()
channel = setup.get_channel()


def send():    
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        res = json.loads(url.read().decode())

    days = []
    results = []

    for i in res:
        days.append(i["data"][5:10])
        v = 0.0
        v = (i["totale_casi"] / i["tamponi"]) * 100
        results.append(v)
    

    plt.rcParams.update({'xtick.labelsize': 4})

    plt.figure("Risultati COVID-19 Italia", figsize=(9.0, 5.0))
    plt.ylabel("[contagi/tamponi]%")
    plt.plot(days, results, 'b-+')
    plt.grid()

    strImg = "img.png"
    if os.path.isfile(strImg):
        os.remove(strImg)   

    plt.savefig(strImg,  dpi=800, bbox_inches='tight')
    bot.sendImage(token, channel)   
    
    return

schedule.every().day.at("19:30").do(send)

while True:
    schedule.run_pending()
    time.sleep(60)


    





        
    
    
    