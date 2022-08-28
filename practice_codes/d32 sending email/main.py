import smtplib
my_email = "mic472003@gmail.com"
password = "Suraj@473"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="mihirchauhan473@gmail.com",
        msg="Subject: Hello\n\n This is the body ")