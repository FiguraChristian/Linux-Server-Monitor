import os
import psutil 
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Braucht für Cronjob kompletten Pfad, weil Skript sonst im Userkontext läuft und nicht funktioniert
load_dotenv("/home/christian/projekte/homelab/monitoring/.env")

# Credentials befinden sich in separater .env file
mail_adress = os.getenv("mail_adress")
password = os.getenv("gmail_app_password")

# Achtung, disk_usage braucht Pfad, daher "/", um gesamte Platte zu prüfen
used_ram = psutil.virtual_memory().percent
used_cpu = psutil.cpu_percent()
used_disk_space = psutil.disk_usage("/").percent


# Funktion für Aufbau der Mail
def send_alert(text):
    msg = MIMEText(text)
    msg["To"] = mail_adress
    msg["From"] = mail_adress
    msg["Subject"] = "Ubuntu Server Alert"

    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(mail_adress, password)
        server.send_message(msg)


# Definieren von kritischen Schwellwerten für RAM, CPU und Disk
if used_ram > 90:
    try:
        send_alert(f"RAM-Auslastung kritisch: {used_ram} %")
    except:
        print("Fehler beim versenden der Mail")

if used_cpu > 90:
    try:
        send_alert(f"CPU-Auslastung kritisch: {used_cpu} %")
    except:
        print("Fehler beim Versenden")

if used_disk_space > 85:
    try:
        send_alert(f"Speicherplatz kritisch: {used_disk_space} %")
    except:
        print("Fehler beim Versenden")



