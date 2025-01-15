import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Retrieve SMTP details from environment variables or GitHub secrets
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'swapnilko@gmail.com'
SMTP_PASSWORD = 'InfoSec@2022'
TO_EMAIL = 'swapnil_konde@hotmail.com'
SUBJECT = 'Test Email'
BODY = 'This is a test email sent from GitHub Actions pipeline.'

# Create the message
msg = MIMEMultipart()
msg['From'] = SMTP_USER
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT

# Add body to email
msg.attach(MIMEText(BODY, 'plain'))

# Establish connection and send email
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure the connection
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
    server.quit()
