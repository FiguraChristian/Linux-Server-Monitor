# Linux Server Monitor
Ein automatisiertes Monitoring-Tool, das RAM, CPU und Festplattenauslastung eines Linux-Servers überwacht und bei Überschreitung kritischer Schwellenwerte automatisch eine Warn-E-Mail versendet.

<img width="960" height="253" alt="image" src="https://github.com/user-attachments/assets/4e62a086-c61c-4ae8-b607-d6265dea6c08" />





# Hauptfunktionen
- RAM-Monitoring: Überwacht die Arbeitsspeicherauslastung in Echtzeit
- CPU-Monitoring: Erkennt kritische Prozessorauslastung
- Disk-Monitoring: Überwacht den verfügbaren Festplattenplatz
- E-Mail-Alert: Versendet automatische Warnmeldungen via Gmail SMTP
- Cron-Job: Stündliche automatische Ausführung auf dem Linux-Server

# Tech Stack
- Python 3
- psutil (Systemressourcen-Auslesen)
- smtplib (E-Mail-Versand via Gmail SMTP)
- python-dotenv
