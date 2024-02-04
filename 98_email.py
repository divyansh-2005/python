import smtplib

sender = "kumbhatd@rknec.edu"
recevier = "recevier@gmail.com"
password = "useyourpassword"
subject = "Python email test"
body = "I wrote an email!"

#header
message = f"""From: Divyansh{sender}
To: Namrata{recevier}
subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:  
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,recevier,message)
    print("Email hass been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")