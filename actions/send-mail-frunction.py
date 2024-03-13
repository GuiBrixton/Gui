import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# Created by: Agnaldo Cavaleiro (gui)
# Fecha: 13/03/2024 :)

remitente    = os.environ["FROM"]
destinatario = os.environ["TO"]
asunto       = os.environ["SUBJET"]
passgmail    = os.environ["TOKENGMAIL"]
cuerpo_html = body = """\
<html>
<head>
<style>
  .boton {
      background-color: #089cff;
      color: white;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 5px;
  }
</style>
</head>
<body>
    <h1>Welcome</h1>
    <p><a href="" class="boton">Click</a></p>
</body>
</html>
"""

def enviar_email(remitente, destinatario, asunto, cuerpo_html ):


  try:
    # Configurar el servidor SMTP
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.starttls()
  
    smtp.login('guistarcksoft@gmail.com', passgmail)
   
    # Crear mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remitente
    mensagem['To'] = destinatario
    mensagem['Subject'] = asunto

    # Adicionar el cuerpo  e-mail
    mensagem.attach(MIMEText(cuerpo_html, 'html'))


    # Enviar e-mail
    smtp.sendmail(remitente, destinatario, mensagem.as_string())
    smtp.quit()


    return True
  except Exception as e:
    print(f"Error sending email: {e}")
    return False
  
resultado = enviar_email(remitente, destinatario, asunto, cuerpo_html)

if resultado:
  print("¡El correo electrónico se ha enviado correctamente!")
else:
  print("Error al enviar el correo electrónico.")
  sys.exit(1)
