import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "devmax70@gmail.com"
host_pass = "*****"
guest_address = "devmax72@gmail.com"
subject = "Regarding failure of main.py"
content = '''Hello, 
				Developer this is an email regarding to your last commit. It seems that your main.py is not working properly please check it once and recommit.
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')



