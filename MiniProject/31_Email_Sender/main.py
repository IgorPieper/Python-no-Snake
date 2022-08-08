import smtplib

my_email = "yourmail@mail.com"
password = "haslo1234"
location = "smtp.mail.com"

with smtplib.SMTP(location) as connect:
    connect.starttls()
    connect.login(user=my_email, password=password)
    connect.sendmail(
        from_addr=my_email,
        to_addrs="someonemail@mail.com",
        msg="Subject:Title\n\nThis is my Mail!"
    )
