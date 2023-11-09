import smtplib


def send_email(sender, password, recipient, subject, message):
    try:
        server = smtplib.SMTP('smtp.qq.com', 25)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, f'Subject: {subject}\n\n{message}')
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))


if __name__ == '__main__':
    send_email("your.qq.email@example.com", "your QQ email password", "recipient@example.com", "Subject", "Message")
