##################### Extra Hard Starting Project ######################

import pandas
import datetime as dt

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


df = pandas.read_csv("birthdays.csv")
df_dict = df.to_dict('records')



today = dt.datetime.today()
today_tuple = (today.month, today.day)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




