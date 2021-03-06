""" Bulk mailer script """

import json
import smtplib
import time

EMAIL_LIST = []

# Read config file
with open("./CONFIG.json", "r") as file:
    CONFIG = json.loads(file.read())
file.close()

# Read mailing list and add it to EMAIL_LIST
with open("./mailing_list.txt", "r") as file:
    while True:
        LINE = file.readline()
        if not LINE:
            break
        else:
            EMAIL_LIST.append(LINE.strip())
file.close()

# Construct the message to be sent.
MESSAGE = "SUBJECT: {} \n\n{}".format(CONFIG["subject"], CONFIG["message"])

# Open SMTP secure connection.
EMAIL_SERVER = smtplib.SMTP_SSL(CONFIG["smtp"], CONFIG["port"])
# Login
EMAIL_SERVER.login(CONFIG["smtp_username"], CONFIG["password"])
# Send emails to emails in EMAIL_LIST in a loop
for email in EMAIL_LIST:
    EMAIL_SERVER.sendmail(CONFIG["from_email"], email, MESSAGE)
    time.sleep(0.5)

# Quit SMTP server
EMAIL_SERVER.quit()
