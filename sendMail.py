# Sends a email when called that says the test is complete
# The emails must be set to the people who need to receive the email
# emails = "name@place.com,nextname@again.com,next@web.com"

import smtplib as s

def send():
    user = "mech.testing.pi@gmail.com"
    password = "RPi@Icon"

    emails = "grant.bruneel@iconfitness.com"
    toWho = emails.split(",")
    
    subject = "Test is complete"
    header = "To: " + emails + "\nFrom: " + user + "\nSubject: " + subject
    body = "The test the raspberry pi was running is complete"

    sending = s.SMTP("smtp.gmail.com", 587)
    
    sending.ehlo()
    sending.starttls()
    sending.ehlo()

    sending.login(user, password)
    sending.sendmail(user, toWho, header + "\n\n" + body)

    sending.quit()

send()