#!/usr/bin/python3
import requests, telegram_send, datetime, time, schedule

def report():
    print('Report: Successful connection!')
    telegram_send.send(messages=["Daily Report: Connection successful!"])


while True:
    r = requests.get('https://www.kcell.kz/', verify='./kcellkz.pem')
    print(r.status_code)
    if r.status_code == 200:
        # now = datetime.datetime.now()
        schedule.every(1).hours.do(report)
    else:
        print('Connection lost')
        telegram_send.send(messages=["Something went wrong!"])

    schedule.run_pending()
    time.sleep(300)
