# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Text of E-Mail")


# Open the plain text file whose name is in textfile for reading.
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of textfile'
msg['From'] = "mylogin@yandex.ru"
msg['To'] = "mylogin@gmail.com"

# Send the message via our own SMTP server.
# s = smtplib.SMTP('localhost')
# https://stackoverflow.com/questions/20349170/socket-error-errno-111-connection-refused
s = smtplib.SMTP(host='smtp.yandex.ru', port=465)

# https://docs.python.org/2/library/smtplib.html#smtplib.SMTP.starttls
s.send_message(msg)
s.quit()