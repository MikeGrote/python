
import smtplib
from smtplib import SMTPException

sender = 'test@testi4.de'
receivers = ['sap-stadtwerk-hassfurt@incept4.de']

message = """From: From Person <test@testi4.de>
To: To Person <sap-stadtwerk-hassfurt@incept4.de>
Subject: A000007086038 - Approve Document

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('linuxhptn.incept4.local:25000')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException as e:
   print (e.smtp_code)
   print (e.smtp_error)

try:
   smtpObj = smtplib.SMTP('hasql1d0.sap.psmanaged.com:25000')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException as e:
   print (e.smtp_code)
   print (e.smtp_error)