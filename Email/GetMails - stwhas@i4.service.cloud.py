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


         receivers = ['stwhas@i4service.cloud']
         try:
             smtpObj = smtplib.SMTP('hasql1d0.sap.psmanaged.com:25000')
             smtpObj.sendmail(email_message['From'], receivers, email_body)         
             print ("Successfully sent email")
         except SMTPException as e:
             print (e.smtp_code)
             print (e.smtp_error)


         clear_inbox(conn, emailid, "Archiv")

     
    except IndexError:
         print("No new email")
 
    conn.close()
    conn.logout()


parser = argparse.ArgumentParser()
parser.add_argument('-mpass', '-mailbox_password', dest = 'mailbox_password', help = 'mailbox password.')
args = parser.parse_args()
 
user = 'stwhas@i4service.cloud'
mailbox_password = 'Duq70923' #args.mailbox_password

start()
