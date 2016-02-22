
import smtplib

fromaddr = 'davyanhoneyghan@gmail.com'
toaddr  = 'davyanhoneyghan@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'davyanhoneyghan@gmail.com'
password = '{youremailapppassword}''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()
