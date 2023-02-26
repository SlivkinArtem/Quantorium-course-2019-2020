from tkinter import *
import smtplib

from email.mime.image import MIMEImage
from email.mime. text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(event):
    msg = MIMEMultipart()
    message = message_entry.get(1.0, END)

    password = pass_entry.get()
    msg['From'] = em_entry.get()
    msg['To'] = to_entry.get()
    msg['Subject'] = 'kek'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    # запуск сервера
    server.starttls()
    # авторизация на сервере
    server.login(msg['From'], password)
    # отправка письма
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    # выход из текущей сессии
    server.quit()

    print(f'Успешно отправлено', {msg['To']})

root = Tk()
root.title('Message Visualization')
root.geometry('400x300')
lb = Label(text = 'Ваш email', fg = '#525454')
lb.place(x = 5, y = 10)
em_entry = Entry()
em_entry.place(x =70, y = 10)

lb2 = Label(text = 'Пароль', fg = '#525454')
lb2.place(x = 5, y = 45)
pass_entry = Entry()
pass_entry.place(x = 70, y = 45)

lb3 = Label(text = 'Кому', fg = '#525454')
lb3.place(x = 5, y = 80)
to_entry = Entry()
to_entry.place(x = 70, y = 80)

message_entry = Text(width=30, height= 10)
message_entry.place(x = 5, y = 110)
message_entry.bind("<Return>", send_mail)



root.mainloop()

