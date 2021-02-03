# Hochwasser-Alarm mit Push

Python Skript der innerhalb kurzester Zeit entworfen wurde und diesbezüglich nicht mit vollständiger funktionsweise ausgestattet.

Dieser Schickt dir 10 Push Nachrichten auf deinem Smartphone, als Alarm beim Erreichen/Überlaufen der Festgelegten Grenze. 

![Hochwasseralarm Skript](https://i.ibb.co/5hzPF1S/hochwasseralarm-in-action.png)

## Installation

Um den Script zu benutzen, brauchst du dein API Access Tokens von hier:

```bash
https://www.pushbullet.com
```
desto weiteres benötigst du diese beide Ressourcen, um den Script auf Linux Server Starten zu können:
```bash
pip install beautifulsoup4
sudo apt-get install python3-lxml
```
Der Grund dafür ist einfach, man braucht kein eigenes Hosting & Deployment ist auf allen Systemen verfügbar. 

Momentan läuft dieser Script auf einem Debian Server!

Eine Unabhängige Version ist jedoch in Entwicklung.

## Hardcoded Stuff
Diese Sachen kann man Beliebig ändern:
```python
import foobar

limiter = 700 
#Set your Alarm Limit for Notifications

limiter_2 = 690 
#Set your Warning Limit

time.sleep(1800) 
#Set Refresh-Rate for Data Pull in seconds
#Default is 30 Minutes
```
Diese Variablen werden in Zukunft durch GUI ersetzt!

## Developer(s)
- auxii#0001