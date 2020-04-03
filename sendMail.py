import smtplib as s

def send():
    user = "mech.testing.pi@gmail.com"
    password = "RPi@Icon"

    toWho = "mech.testing.pi@gmail.com"
    
    subject = "Test is complete"
    header = "To: " + toWho + "\nFrom: " + user + "\nSubject: " + subject
    body = "The test the raspberry pi was running is complete"

    sending = s.SMTP("smtp.gmail.com", 587)
    
    sending.ehlo()
    sending.starttls()
    sending.ehlo()

    sending.login(user, password)
    sending.sendmail(user, toWho, header + "\n\n" + body)

    sending.quit()
