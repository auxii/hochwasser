from bs4 import BeautifulSoup
from datetime import date, datetime
import time
import requests
import json

#Hardcoded Data
limiter = 701
today = date.today()
today = today.strftime("%d.%m.%Y")
alive = True

while alive == True:
    def data_raw():
        time.sleep(10)
        # Online Database for Data
        source = requests.get('https://www.hochwasser-rlp.de/karte/einzelpegel/flussgebiet/rhein/teilgebiet/mittelrhein/pegel/OBERWINTER/darstellung/tabellarisch').text
        soup = BeautifulSoup(source, 'lxml')

        # Local File for Development
        #with open('index.html') as html_file:
        #    soup = BeautifulSoup(html_file, 'lxml')

        rows = soup.find("table", class_="wasserstaende").find("tbody").find_all("tr")

        for row in rows:
            cells = row.findAll("td")
            report_date = cells[0].get_text()
            report_time = cells[1].get_text()
            report = cells[2].get_text()

            if int(report) == limiter or int(report) > limiter:
                if report_date == today:
                    limit_reached(report, today, report_time)
                    #break
                else:
                    print(
                        "Datum: " + report_date + " │ Uhrzeit:" + report_time + " │ Rheinstand: " + report + " Meter" + " LIMIT WAS REACHED!")

            else:
                print("Datum: " + report_date + " │ Uhrzeit:" + report_time + " │ Rheinstand: " + report + " Meter")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Data Refreshed at: " + current_time)

    def limit_reached(report, today, report_time):
        #playsound("/path/to/.mp3")
        print("ALARM! DER LIMIT WURDE ÜBERSCHRITTEN!!!!")
        print("Heutiger Datum: " + today)
        print("Uhrzeit: " + report_time)
        print("Wasserstand: " + report)
        pushbullet_message(report, report_time)

    def pushbullet_message(report, report_time):
        for i in range(10):
            msg = {"type": "note", "title": "Wasserpegel Limit erreicht um: " +report_time, "body": "Aktueller Wasserstand: " + report + " meter!"}
            TOKEN = '#########'
            resp = requests.post('https://api.pushbullet.com/v2/pushes',
                                 data=json.dumps(msg),
                                 headers={'Authorization': 'Bearer ' + TOKEN,
                                          'Content-Type': 'application/json'})
            if resp.status_code != 200:
                raise Exception('Error', resp.status_code)
            else:
                print('Message sent to Device!')
        after_alert()

    def after_alert():
        exit()

    data_raw()