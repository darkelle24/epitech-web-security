
from config import JWT_VALIDATION_KEY, EMAIL_SENDER_ADDR, EMAIL_SENDER_PASSWD
import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from jinja2 import Environment, FileSystemLoader
import jwt


def validate_email_addr(user):
    try:
        addr_from = str(EMAIL_SENDER_ADDR)
        addr_to = user.email
        password = str(EMAIL_SENDER_PASSWD)
        server = smtp.SMTP_SSL("ssl0.ovh.net", 465)
        server.set_debuglevel(1)
        server.ehlo()
        # server.starttls()
        server.login(addr_from, password)

        jwt_code = jwt.encode({'user': str(user.id), 'email': str(
            user.email)}, JWT_VALIDATION_KEY, algorithm='HS256')

        # file_loader = FileSystemLoader('app/services/email/templates')
        # env = Environment(loader=file_loader)

        # template = env.get_template('validate_email.html')
        # output = template.render(
        #     link="http://localhost:5000/users/email/validate/" + jwt_code, name=user.username)

        output = "http://localhost:5000/users/email/validate/" + jwt_code

        message = MIMEText(output, 'html')
        message['Subject'] = "Validate your Email address"
        message['From'] = formataddr(
            (str(Header('Attack Defend', 'utf-8')), addr_from))
        message['To'] = addr_to

        server.sendmail(addr_from, [addr_to], message.as_string())
        server.quit()
    except smtp.SMTPServerDisconnected:
        print("The SMTP Server has been disconnected")
    except smtp.SMTPResponseException as error:
        print("The SMTP Server send an error : \n", str(
            error.smtp_code), ":", str(error.smtp_error))
    except smtp.SMTPSenderRefused:
        print("The SMTP Server refused to accept the sender address")
    except smtp.SMTPRecipientsRefused:
        print("The SMTP Server refused to accept the receiver address")
    except smtp.SMTPDataError:
        print("The SMTP Server refused to accept the message data")
    except smtp.SMTPConnectError:
        print("Error occured during establishment of a connection with the server")
    except smtp.SMTPHeloError:
        print("The server refused our HELO message")
    except smtp.SMTPNotSupportedError:
        print("The command or option attempted is not supported by the server")
    except smtp.SMTPAuthenticationError:
        print("SMTP authentication went wrong. Most probably the server didn’t accept the username/password combination provided")
