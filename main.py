##################### Extra Hard Starting Project ######################

import os
import pandas
import datetime as dt
import random
import smtplib


# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
df_dict = df.to_dict('records')

# I struggled with this dictionary comprehension. It's a bit more complicated than the ones we've done previously.
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}
print(type(new_dict))


today = dt.datetime.today()
today_tuple = (today.month, today.day)

# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in new_dict:
    letter_number = random.randint(1, 3)
    letter_t = f"letter_templates/letter_{letter_number}.txt"
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(letter_t) as letter:
        data = letter.read()
        new_letter = data.replace("[NAME]", new_dict[today_tuple]["name"])
        print(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
sender = "<johan@example.com>"
receiver = new_dict[today_tuple]["email"]

message = f"""\
From: {sender}
To: {receiver}
Subject: Hi Mailtrap\n\n
{new_letter}"""

with smtplib.SMTP("smtp.mailtrap.io", 587) as smtp:
    smtp.starttls()
    smtp.login("6e9cda1e96c233", os.environ.get("MAILTRAP_PASSWORD"))
    smtp.sendmail(sender, receiver, message)




