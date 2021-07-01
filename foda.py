import smtpd, ssl
import smtplib

def enviar(texto):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "projetowtic@gmail.com"  # Enter your address
    receiver_email = "luccatsoares@gmail.com"  # Enter receiver address
    password = 'DryFish@2020'
    message = f"{texto}"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return 0