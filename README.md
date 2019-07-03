# RPi-Restart-Notifier
Raspberry Pi Restart Notifier

Reports with external IP when Raspberry restart.

How to Use?

1- Download files and place anywhere.

2- Edit mySettings.py file.
Turn on setting in sender Gmail at link below:
https://myaccount.google.com/lesssecureapps


3- Add cronjob with "sudo crontab -e"

This line:

@reboot sleep 60 && python /where/is/files/RUN.py >> /where/is/files/LOGS.txt 2>&1 &

File permissions:
py files: executable
txt files: writable


Raspberry yeniden başladığında Rapberry' nin dış IP' sini size bildirir.

Nasıl Kullanılır?

1- Dosyaları indirin ve herhangi bir yere koyun.

2- mySettings.py dosyasını düzenleyin.
Gönderen Gmail adresi için aşağıdaki linkteki ayarı açın:
https://myaccount.google.com/lesssecureapps

3- Zamanlanmış görevlere "sudo crontab -e" komutu ile aşağıdaki satırı ekleyin:

@reboot sleep 60 && python /where/is/files/RUN.py >> /where/is/files/LOGS.txt 2>&1 &

py dosyalarını çalıştırılabilir, txt dosyalarını yazılabilir yapın.
