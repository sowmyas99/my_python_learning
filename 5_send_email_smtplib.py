#5) use python to send emails
# Import smtplib for the actual sending function

import smtplib

fromaddr = "sowmya.jenkins@gmail.com"
toaddrs  = "sowmya.jenkins@gmail.com"
password = input("Type your password and press enter: ")
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

message = """\
Subject: Hi Hello

This is a test message sent from Python."""

print("Message length is", len(message))
smtp_server = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp_server,port)
server.set_debuglevel(1)
server.starttls()
server.login(fromaddr, password)

server.sendmail(fromaddr, toaddrs, message)
server.quit()