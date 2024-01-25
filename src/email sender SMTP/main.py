import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        my_email = "testingsketch@gmail.com"
        password = "eqhp ioap ivud rrpb"
        with smtplib.SMTP('email sender SMTP.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="vikasgole089@gmail.com",
                                msg=f"subject: Thursday motivational quote\n\n{quote}")
        print(quote)







