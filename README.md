# Linux Server Monitor
Ein automatisiertes Monitoring-Tool, das RAM, CPU und Festplattenauslastung eines Linux-Servers überwacht und bei Überschreitung kritischer Schwellenwerte automatisch eine Warn-E-Mail versendet, einen Incident im Service Now erstellt und einem Fachbereich zuweist.

# Erstellung und Auto Assignment Incident
<img width="960" height="362" alt="SNOW" src="https://github.com/user-attachments/assets/bdac415b-8737-4dac-bf90-97047c68de47" />


# Warning per Mail
<img width="960" height="200" alt="Mail" src="https://github.com/user-attachments/assets/a1f211ef-3c7a-4445-a256-1d291e5cc4a9" />


# Hauptfunktionen
- RAM-Monitoring: Überwacht die Arbeitsspeicherauslastung in Echtzeit
- CPU-Monitoring: Erkennt kritische Prozessorauslastung
- Disk-Monitoring: Überwacht den verfügbaren Festplattenplatz
- E-Mail-Alert: Versendet automatische Warnmeldungen via Gmail SMTP
- Service Now: Erstellung und Auto Assignment von Incidents
- Cron-Job: Stündliche automatische Ausführung auf dem Linux-Server

# Tech Stack
- Python 3
- psutil (Systemressourcen-Auslesen)
- smtplib (E-Mail-Versand via Gmail SMTP)
- python-dotenv (für die sichere Verwendung meiner privaten informationen)
- Service Now (Enterprise Tickettool) 
