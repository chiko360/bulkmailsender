# -*- coding: utf-8 -*-
"""
@author: chafik maouche
facebook: https://www.facebook.com/ch1k0360
github: https://github.com/chiko360

"""

print("                                                                    ")
print("        __        _   __               ______    ______     ____    ")  
print("       [  |      (_) [  |  _          / ____ `..' ____ \  .'    '.  ")
print(" .---.  | |--.   __   | | / ]  .--.   `'  __) || |____\_||  .--.  | ")
print("/ /'`\] | .-. | [  |  | '' < / .'`\ \ _  |__ '.| '____`'.| |    | | ")
print("| \__.  | | | |  | |  | |`\ \| \__. || \____) || (____) ||  `--'  | ")
print("'.___.'[___]|__][___][__|  \_]'.__.'  \______.''.______.' '.____.'  ")
print("                         mass mail sender                           ")
      
import smtplib
sender_mail = input('entre the sender gmail address : ')
sender_pass =input('entre the sender gmail password : ')
smtp = smtplib.SMTP('smtp.gmail.com')
smtp.connect('smtp.gmail.com', '587')
smtp.starttls()
smtp.ehlo()
smtp.login(str(sender_mail),str(sender_pass))
s = input("entre your email subject : ")
with open('logins.txt','r') as combo:
    with open('mail.txt','r') as mail:
        i=1
        combo_contents = ""
        mail_contents = ""
        for i in range(sum(1 for line in open('combo.txt'))):
            combo_contents = combo.readline()
            subject = s
            body = combo_contents
            msg = f'Subject: {subject}\n\n{body}'
            mail_contents = mail.readline()
            smtp.sendmail(sender_mail,mail_contents, msg)
input("emails has been sent succesfully")