import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail_gonder(gonderici, sifre, alici, konu, icerik):
    msg = MIMEMultipart()

    msg['From'] = gonderici
    msg['To'] = alici
    msg['Subject'] = konu

    msg.attach(MIMEText(icerik, 'plain'))

    try:
        mail = smtplib.SMTP('smtp.office365.com', 587)

        mail.ehlo()
        mail.starttls()

        mail.login(gonderici, sifre)

        mail.sendmail(gonderici, alici, msg.as_string())
        print("E-posta gönderildi.")

        mail.close()

    except Exception as e:
        print("E-posta gönderme hatası:", str(e))


gonderici = input("Gönderici e-posta adresini girin: ")
sifre = input("Gönderici e-posta şifresini girin: ")
alici = input("Alıcı e-posta adresini girin: ")
konu = input("E-posta konusunu girin: ")
icerik = input("E-posta içeriğini girin: ")
aralik = int(input("E-postalar arasındaki süreyi saniye cinsinden girin: "))
adet = int(input("Kaç adet e-posta göndermek istediğinizi girin: "))


for i in range(adet):
    mail_gonder(gonderici, sifre, alici, konu, icerik)
    time.sleep(aralik)

