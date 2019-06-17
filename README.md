# RPi-Restart-Notifier
Raspberry Pi Restart Notifier

Reports with external IP when Raspberry restart.

How to Use?

1- Download files and place anywhere.

2- Edit mySettings.py file.

3- Add cronjob with "sudo crontab -e"
@reboot sleep 60 && python /where/is/files/RUN.py >> /where/is/files/LOGS.txt 2>&1 &
