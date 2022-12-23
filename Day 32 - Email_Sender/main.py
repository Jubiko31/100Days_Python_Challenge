import smtplib
import datetime as dt
import pandas as pd
# Here tested for real credentials,
# also you can add real users in csv and progema will send template letter on their bd
email = "<email>"
password = "<app-password>"

today = dt.datetime.now()
today_t = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

bd_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_t in bd_dict:
    bd_boy = bd_dict[today_t]
    filepath = "letter_templates/letter_1.txt"
    with open(filepath) as letter:
        content = letter.read()
        content = content.replace("[NAME]", bd_boy["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendmail(
            from_addr=email, 
            to_addrs=bd_boy["email"], 
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )