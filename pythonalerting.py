import os
import psutil 
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests

# hard path needed for cron job
load_dotenv("/home/christian/projekte/homelab/monitoring/.env")

# get GMAIL Credentials from .env
mail_adress = os.getenv("mail_adress")
gmail_password = os.getenv("gmail_app_password")

# get Service Now Credentials from .env
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


# disk_usage needs path, so "/" (from root)
hostname = os.uname().nodename
used_ram = psutil.virtual_memory().percent
used_cpu = psutil.cpu_percent()
used_disk_space = psutil.disk_usage("/").percent


# Function Mail
def send_alert(text):
    msg = MIMEText(text)
    msg["To"] = mail_adress
    msg["From"] = mail_adress
    msg["Subject"] = "Ubuntu Server Alert"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(mail_adress, gmail_password)
        server.send_message(msg)



# Function INC creation with few parameters
def create_incident(inc_description):

    incident_data = {
    "short_description" : inc_description,
    "caller_id" : "6816f79cc0a8016401c5a33be04be441",
    "assignment_group" : "d625dccec0a8016700a222a0f7900d06 "
}

    # Post Requests INC
    inc_response = requests.post(target_path, auth=(sn_dev_username,sn_dev_pw), headers=headers, json=incident_data)

    if inc_response.status_code == 201:
        print("Incident erfolgreich erstellt")
    else:
        print(f"Fehler bei INC-Erstellung: {inc_response.status_code}")


# Function Error exception
def error_message():
    print("Es ist ein Fehler aufgetreten")


# Set critical limits for RAM, CPU and Disk Space
if used_ram > 90:
    try:
        send_alert(f"RAM-Auslastung kritisch: {used_ram} %")
        create_incident(f"{hostname} RAM-Auslastung kritisch: {used_ram} %")
    except:
        error_message()

if used_cpu > 90:
    try:
        send_alert(f"CPU-Auslastung kritisch: {used_cpu} %")
        create_incident(f"{hostname} CPU-Auslastung kritisch: {used_cpu} %")

    except:
        error_message()

if used_disk_space > 85:
    try:
        send_alert(f"Speicherplatz kritisch: {used_disk_space} %")
        create_incident(f"{hostname} Speicherplatz kritisch: {used_disk_space} %")

    except:
        error_message()