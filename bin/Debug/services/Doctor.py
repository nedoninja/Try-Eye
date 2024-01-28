import smtplib

smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login('d1arama@yandex.ru','qpetjwgrdzkdlkvf')
f = open("services\\acuity.txt", encoding="utf-8")
s = f.read()
f.close()

f = open("services\\doctor.txt", "r", encoding="utf-8")
n = f.read()
f.close()
em, name = n.split()

smtpObj.sendmail("d1arama@yandex.ru", str(em), f"Hi, The patient {name} has {s}")
smtpObj.quit()