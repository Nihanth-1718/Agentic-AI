"""
====================================================
Day 25 - Email Automation with Attachment & Datetime

Topics Covered:

1. Email Automation with Attachment
   - smtplib
   - MIMEMultipart
   - MIMEText
   - MIMEBase
   - encoders
   - File Attachment
   - SMTP Server

2. Datetime Module
   - datetime.now()
   - datetime.today()
   - date()
   - day
   - month
   - year
   - weekday()
   - isoweekday()
   - time()
   - strftime()

====================================================
"""

# ==========================================
# Email Automation with Attachment
# ==========================================

import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print("========== Email Automation ==========")

from_mail = "your_email@gmail.com"
to_mail = "receiver_email@gmail.com"

mail_subject = "Email Automation"

mail_password = "YOUR_APP_PASSWORD"

mail_body = """
Hello,

This email is sent using Python.

This program demonstrates Email Automation
with File Attachment.

Thank You.
"""

attachment_file = "day25.py"      # Change if required

email = MIMEMultipart()

email["From"] = from_mail
email["To"] = to_mail
email["Subject"] = mail_subject

email.attach(MIMEText(mail_body, "plain"))

attachment_part = MIMEBase("application", "octet-stream")

with open(attachment_file, "rb") as file:
    attachment_part.set_payload(file.read())

encoders.encode_base64(attachment_part)

attachment_part.add_header(
    "Content-Disposition",
    f'attachment; filename="{os.path.basename(attachment_file)}"'
)

email.attach(attachment_part)

email_text = email.as_string()

"""
smtp = smtplib.SMTP("smtp.gmail.com", 587)

smtp.starttls()

smtp.login(from_mail, mail_password)

smtp.sendmail(from_mail, to_mail, email_text)

print("Mail Sent Successfully")

smtp.quit()
"""

# ==========================================
# Datetime Module
# ==========================================

from datetime import datetime

print("\n========== Datetime Module ==========")

current_datetime = datetime.now()

print("Current Datetime :", current_datetime)

print("Current Date :", current_datetime.date())

print("Day :", current_datetime.day)

print("Month :", current_datetime.month)

print("Year :", current_datetime.year)

today_date = datetime.today()

print("\nToday :", today_date)

print("Weekday :", today_date.weekday())

print("ISO Weekday :", today_date.isoweekday())

print("Current Time :", today_date.time())

print("\nString Formatting")

print("Week Number :", today_date.strftime("%W"))

print("Month :", today_date.strftime("%m"))

print("Weekday Number :", today_date.strftime("%w"))

print("Day Name :", today_date.strftime("%A"))

print("Month Name :", today_date.strftime("%B"))

print("Date :", today_date.strftime("%d-%m-%Y"))

print("Time :", today_date.strftime("%H:%M:%S"))
