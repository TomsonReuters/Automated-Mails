import smtplib,email,ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = "remitente@gmail.com"
#para gmail hay que autorizar Python desde el chrome
#Abrir el google chrome y activar verificacion en 2 pasos
#luego ir al siguiente link https://myaccount.google.com/u/4/apppasswords
#Seleccionar aplicacion (otra), y la llamaremos Python
#Ello nos permitira tener la contraseña para poder automatizar el envio
#Sin esto no se podra autenticar
email_password = "password" 
email_receiver = ['receptor@gmail.com']
subject = 'titulo'
body = "cuerpo"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
