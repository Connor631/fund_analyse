import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


class auto_mail(object):
    def __init__(self, config_path):
        with open(config_path, "r", encoding="utf8") as fp:
            config = json.load(fp)
        self.sender = config["mail_config"]["sender"]
        self.receiver = config["mail_config"]["recipient"]
        self.password = config["mail_config"]["password"]

    def send_email_df(self, subject, df):
        # 邮件发送者
        sender = self.sender
        # 邮件接收者
        receiver = self.receiver
        # 邮件主题
        subject = subject
        # 邮件内容
        body = df.to_html()

        # 创建一个 multipart message
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject
        # 添加邮件内容
        message.attach(MIMEText(body, "html"))

        # 163邮箱的授权码信息
        username = sender
        password = self.password

        # 通过163邮箱的SMTP服务器发送邮件
        with smtplib.SMTP("smtp.163.com", 25) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, message.as_string())


if __name__ == '__main__':
    pass
