# Setting up the Mailer for Sending the mail
# To run command in a python script
import os
#SMTP- Simple Mail Transfer Protocol
import smtplib
import imghdr 
from email.message import EmailMessage


def mailing(email):
    #Getting Username and Password By Enabling Two Step Authentication and creating App password
    EMAIL_ADDRESS ='securazeta@gmail.com'
    EMAIL_PASSWORD ='atvfpyljjngcyizo'

    contacts = []
    #Storing the Users mail in the list
    contacts.append(email)
    msg = EmailMessage()
    msg['Subject'] = 'File Integrity Monitor - Log Results'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =contacts
    
    msg.set_content('Please Find the attachments')
    #Body of Mail
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h3 style="color:#5c66f2;">Log Results</h3>
            Here are the results for the regular expression that you queried. Please Find the attachments!!!!!!!
            <p style="color:#606060;">With Regards<br>
            Team Securazeta</p>
        </body>
    </html>
    """, subtype='html')
    files=['result.log']
    for file in files:
        with open(file,'rb') as f:
            file_data=f.read()
            file_name=f.name
        #Attaching the File for the Mail
        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

    #Logging into the mail and verfying the sender credentials and Send the mail
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
