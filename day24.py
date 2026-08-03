"""
====================================================
Day 24 - JSON, Collections & Email Automation

Topics Covered:

1. JSON Module
   - dumps()
   - loads()

2. Collections Module
   - Counter

3. SMTP (Simple Mail Transfer Protocol)
   - SMTP Connection
   - starttls()
   - login()
   - sendmail()
   - quit()

4. Email Automation
   - MIMEMultipart
   - MIMEText
   - OTP Generation
   - OTP Verification

====================================================
"""

# ==========================================
# JSON Module
# ==========================================

import json

print("========== JSON Module ==========")

student_data = {
    "name": "Nihanth",
    "age": 21,
    "course": "Agentic AI"
}

print(student_data)
print(type(student_data))

json_string = json.dumps(student_data)

print(json_string)
print(type(json_string))

student_object = json.loads(json_string)

print(student_object)
print(type(student_object))

numbers = json.loads("[10,20,30,40]")

print(numbers)
print(type(numbers))

# ==========================================
# Collections Module
# ==========================================

from collections import Counter

print("\n========== Collections Module ==========")

letter_data = ["A", "B", "C", "A", "A", "C", "B", "A"]

letter_count = Counter(letter_data)

print(letter_count)
print(dict(letter_count))

# ==========================================
# SMTP - Simple Email
# ==========================================

import smtplib

print("\n========== SMTP Example ==========")

from_mail = "your_email@gmail.com"
to_mail = "receiver_email@gmail.com"
mail_password = "YOUR_APP_PASSWORD"

mail_message = "Welcome to my World. This is an automated email."

"""
smtp = smtplib.SMTP("smtp.gmail.com", 587)

smtp.starttls()

smtp.login(from_mail, mail_password)

smtp.sendmail(from_mail, to_mail, mail_message)

print("Mail Sent Successfully")

smtp.quit()
"""

# ==========================================
# Email Automation with OTP
# ==========================================

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

print("\n========== Email Automation ==========")

mail_sender = from_mail
mail_receiver = to_mail

mail_subject = "Regarding Placement"

email = MIMEMultipart()

email["From"] = mail_sender
email["To"] = mail_receiver
email["Subject"] = mail_subject

generated_otp = random.randint(100000, 999999)

mail_body = f"""
Hello,

This is an automated email.

Your OTP is : {generated_otp}

Thank You.
"""

email.attach(MIMEText(mail_body, "plain"))

email_text = email.as_string()

"""
smtp = smtplib.SMTP("smtp.gmail.com", 587)

smtp.starttls()

smtp.login(mail_sender, mail_password)

smtp.sendmail(mail_sender, mail_receiver, email_text)

print("OTP Mail Sent Successfully")

smtp.quit()
"""

# ==========================================
# OTP Verification
# ==========================================

entered_otp = int(input("\nEnter the OTP: "))

if entered_otp == generated_otp:
    print("Login Successful")
else:
    print("Invalid OTP")
