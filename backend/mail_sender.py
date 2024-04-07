
# Send the mail
import smtplib
import os
import dotenv
dotenv.load_dotenv()
class GmailSender:
    def __init__(self,subject,Summary,Rating):
        self.server = "smtp.outlook.com"
        self.from_email = os.environ.get("EMAIL_USER")
        self.to_emails = ["thanabordee.noun@gmail.com"]
        self.subject = subject
        self.text = f"Summary: {Summary}\nRating: {Rating}"
        self.username = os.environ.get("EMAIL_USER")
        self.password = os.environ.get("PASSWORD")
        print(self.username,self.password)
        self.send_email()

    def send_email(self):
        # Prepare actual message
        message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s
        """ % (self.from_email, ", ".join(self.to_emails), self.subject, self.text)

        # Send the mail
        server = smtplib.SMTP(self.server , 587)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.from_email, self.to_emails, message)
        server.quit()

#GmailSender("Review","The food was delicious and the service was excellent. I would definitely recommend this restaurant to my friends.",5)

