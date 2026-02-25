import os
import psutil 
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests

# Braucht für Cronjob kompletten Pfad, weil Skript sonst im Userkontext läuft und nicht funktioniert
load_dotenv("/home/christian/projekte/homelab/monitoring/.env")

# Credentials befinden sich in separater .env file
## Gmail
mail_adress = os.getenv("mail_adress")
gmail_password = os.getenv("gmail_app_password")

## Service Now
sn_dev_instanz = os.getenv("SN_URL")
sn_dev_username = os.getenv("SN_UN")
sn_dev_pw = os.getenv("SN_PW")

# URL INC Table 
incident_url = "/api/now/table/incident"

# create target path
target_path = f"{sn_dev_instanz}{incident_url}"

# send and request JSON
headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}


# Achtung, disk_usage braucht Pfad, daher "/", um gesamte Platte zu prüfen
hostname = os.uname().nodename
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
        server.login(mail_adress, gmail_password)
        server.send_message(msg)



# Funktion für INC-Erstellung im Service Now
def create_incident(inc_description):

    incident_data = {
    "short_description" : inc_description,
    "caller_id" : "6816f79cc0a8016401c5a33be04be441",
    "assignment_group" : "d625dccec0a8016700a222a0f7900d06 "
}

    # Send Requests all INC
    inc_response = requests.post(target_path, auth=(sn_dev_username,sn_dev_pw), headers=headers, json=incident_data)



# Definieren von kritischen Schwellwerten für RAM, CPU und Disk
if used_ram > 20:
    try:
        send_alert(f"RAM-Auslastung kritisch: {used_ram} %")
        create_incident(f"{hostname} RAM-Auslastung kritisch: {used_ram} %")
    except:
        print("Es ist ein fehler aufgetreten")

if used_cpu > 20:
    try:
        send_alert(f"CPU-Auslastung kritisch: {used_cpu} %")
        create_incident(f"{hostname} CPU-Auslastung kritisch: {used_cpu} %")

    except:
        print("Es ist ein fehler aufgetreten")

if used_disk_space > 20:
    try:
        send_alert(f"Speicherplatz kritisch: {used_disk_space} %")
        create_incident(f"{hostname} Speicherplatz kritisch: {used_disk_space} %")

    except:
        print("Es ist ein fehler aufgetreten")



