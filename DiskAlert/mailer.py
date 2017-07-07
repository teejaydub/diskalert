import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

class MailObject(object):
    """
    This object connects to the server and send the mail.

    """

    def __init__(self, server, sender, receivers, subject, text, port=25, user=None, password=None, sender_name=None, tls=True):
        """
        The class initializer.

        Args:
            server (str): The Mail server address
            sender (str): The sender mail address
            receivers (list): The list of mail receivers
            subject (str): The subject for the mail
            text (str): The mail text body. Can be HTML
            port (int): Port to connect to the mail server. Default 25
            user (str): The username to authenticate the mail server. Default None
            password (str): The password to authenticate the mail server. Default None
            sender_name (str): The sender name that should appear in the sent mail. Default None

        """
        self.msg = MIMEMultipart('alternative')

        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.sender_name = sender_name
        self.text = text
        self.tls = tls

        send_status = False
        if self.remoteconn() and self.sender != '' and len(receivers) != 0:
            send_status = self.send()
        if send_status:
            print("Mail sent!")
        else:
            print("Mail transaction failed...")

    def send(self):
        """
        Args:
            subject (string): Email Subject
            receivers (list): List of receivers ex: ['bill@microsoft.com', 'page@google.com']
            text (string): Text message to send

        Returns:
            boolean: True if successfull, False otherwise

        """
        try:

            COMMASPACE = ", "

            self.msg['From'] = formataddr((str(Header(self.sender_name, 'utf-8')), self.sender))
            self.msg['Subject'] = self.subject
            to_text = COMMASPACE.join(self.receivers)
            self.msg['To'] = to_text
            self.msg.attach(MIMEText(self.text, 'html'))
            self.smtpObj.sendmail(self.sender, self.receivers, self.msg.as_string())
            self.smtpObj.quit()
            return True
        except Exception as err:
            print("Error while sending email: {0}".format(str(err)))
            return False

    def remoteconn(self):
        """
        Connects to the Mail server using TLS if set
        Returns:
            boolean: True if successfull, False otherwise

        """
        try:
            self.smtpObj = smtplib.SMTP(self.server, self.port)
            if self.tls:
                self.smtpObj.starttls()
            self.smtpObj.login(self.user, self.password)
            return True
        except Exception as err:
            print("Error while authenticating to the server: {0}".format(str(err)))
            return False

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.smtpObj.quit()
        except:
            pass
