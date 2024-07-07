import smtplib
from tts import print_speak
import recognition

input_func = recognition.define_input()

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    sender_email = 'your_email@gmail.com'
    password = 'your_app_password'
    server.login(sender_email, password)
    server.sendmail(sender_email, to, content.as_string())
    server.quit()

def plain_email():
    try:
        print_speak('MESSAGE')
        content = input_func()
        to = 'receiver_email@gmail.com'
        send_email(to, content)
        print_speak("Email has been sent!")
    except (RuntimeError, TypeError, NameError):
        pass
    except Exception as e:
        print(e)
        print_speak("I am not able to send this email")
        
def with_attachment():
    try:
        import ssl
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        print_speak("what is the subject")
        subject = input_func()
        print_speak("what is the body")
        body = input_func()
        sender_email = 'your_email@gmail.com'
        receiver_email = 'receiver_email@gmail.com'
        password = 'your_app_password'
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email 
        message.attach(MIMEText(body, "plain"))
        print_speak("Which file you want me to send?")
        filename = input(':')
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print_speak("Email has been sent!")
    except (RuntimeError, TypeError, NameError):
        pass
    except Exception as e:
        print(e)
        print_speak("I am not able to send this email")

def email_type():
    print_speak("should send plain email or with attachment")
    input_selected = str(input_func())
    while input_selected != 'plain email' and input_selected != 'attachment':
        print_speak('Please choose a proper input type.\nplain email or attachment?')
        input_selected = input_func()
    if input_selected == 'plain email' or input_selected == 'plain':
        return plain_email()
    else:
        return with_attachment()
    
