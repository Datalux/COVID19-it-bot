# COVID19-it-bot
Un bot di Telegram per il monitoraggio dei casi di COVID19 in Italia. L'operazione effettuata è: contaggi/tamponi-effettuati.
Vedi (https://github.com/Datalux/contagi-covid19-it).

Codice sorgente del bot Telegram **Contagi COVID-19 Italia** (https://t.me/covid19_it).



# Creare una propria instanza
## Requisiti
- schedule
- time
- urllib.request
- json 
- matplotlib

## Installazione 

1. Eseguire `git clone https://github.com/Datalux/COVID19-it-bot` o scaricare il .zip della repository
2. Creare un file `config.json` con la seguente struttura:
```
{
    "token": "110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw",
    "channel" : "@my_channel_name"
}
```
3. Lanciare `python3 run.py`
