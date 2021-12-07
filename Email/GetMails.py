#GetMails.py -mpass "your4incept."

from email.message import EmailMessage
import email
import imaplib
import re
import sys
import logging
import base64
import email.parser
import html2text
import requests
import json
import argparse
import smtplib
from smtplib import SMTPException
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


 
def get_email_body(body):
 
       if body.is_multipart():
         for payload in body.get_payload():
             print('To:\t\t', body['To'])
             print('From:\t', body['From'])
             print('Subject:', body['Subject'])
             print('Date:\t',body['Date'])
             for part in body.walk():
               if (part.get_content_type() == 'text/plain') and (part.get('Content-Disposition') is None):
                output = part.get_payload()
       else:
         print('To:\t\t', body['To'])
         print('From:\t', body['From'])
         print('Subject:', body['Subject'])
         print('Date:\t', body['Date'])
         print('Thread-Index:\t', body['Thread-Index'])
         text = f"{body.get_payload(decode=True)}"
         html = text.replace("b'", "")
         h = html2text.HTML2Text()
         h.ignore_links = True
         output = (h.handle(f'''{html}''').replace("\\r\\n", ""))
         output = output.replace("'", "")
         # output in one line
         #output = output.replace('\n'," ")
         output = output.replace('*', "")
         return output
 
def clear_inbox(conn, emailid ,dest_folder):
    output=[]
    result = conn.uid('COPY', emailid, dest_folder)
    output.append(result)
    print (result)
    if result[0] == 'OK':
     result = mov, data = conn.uid('STORE',emailid, '+FLAGS', '(\Deleted Items)')
     conn.expunge()

def start():
    conn = imaplib.IMAP4_SSL("outlook.office365.com")
    print(user)
    print(mailbox_password)
    conn.login(user,mailbox_password)
    conn.select("Inbox")
     
    try:
     
      resp, items = conn.uid("search",None, 'All')
      items = items[0].split()
      # print(items)
      for emailid in items:
       resp, data = conn.uid("fetch",emailid, "(RFC822)")
       if resp == 'OK':
         email_body = data[0][1].decode('utf-8')
         email_message = email.message_from_string(email_body)
         subject = email_message["Subject"]
         #print (subject)
         #print (email_message)
         #print (email_body)
         
         output =  get_email_body(email_message)
         print (output)
       

         receivers = ['sap-stadtwerk-hassfurt@incept4.de']
         try:
             smtpObj = smtplib.SMTP('hasql1d0.sap.psmanaged.com:25000')
             smtpObj.sendmail(email_message['From'], receivers, email_body)         
             print ("Successfully sent email")
         except SMTPException as e:
             print (e.smtp_code)
             print (e.smtp_error)

         #if subject.lower().startswith('Darktrace'.lower()):
         
         #print(output)
         #do some task
         # move emails to Processed folder and clear Inbox
         clear_inbox(conn, emailid, "Archiv")
         #else:
         #  clear_inbox(conn, "backup")
     
    except IndexError:
         print("No new email")
 
    conn.close()
    conn.logout()

def main():
    scheduler = BlockingScheduler()
    #scheduler.add_job(start, 'interval', max_instances=1, seconds=10)
    scheduler.add_job(start, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
    try:
        scheduler.start()
    except KeyboardInterrupt:
        pass
    scheduler.shutdown()

parser = argparse.ArgumentParser()
parser.add_argument('-mpass', '-mailbox_password', dest = 'mailbox_password', help = 'mailbox password.')
args = parser.parse_args()
 
user = 'team@incept4.de'
mailbox_password = args.mailbox_password

start()
