import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Created by: Agnaldo Cavaleiro (Rulis)
# Fecha: 13/03/2024


remitente    = os.environ["FROM"]
destinatario = os.environ["TO"]
asunto       = os.environ["SUBJET"]
passgmail    = os.environ["TOKENGMAIL"]
cuerpo_html = "<html><body><h1>Hello!</h1><p>This is an Email with HTML body.</p></body></html>"


def enviar_email(remitente, destinatario, asunto, cuerpo_html ):


  try:
    # Configurar el servidor SMTP
    smtp = smtplib.SMTP('smtp.gmail.com', 465)
    smtp.starttls()
    smtp.login('terainntech@gmail.com', passgmail)
   
    # Crear mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remitente
    mensagem['To'] = destinatario
    mensagem['Subject'] = asunto


    # Adicionar el cuerpo  e-mail
    mensagem.attach(MIMEText(cuerpo_html, 'plain'))


    # Enviar e-mail
    smtp.sendmail(remitente, destinatario, mensagem.as_string())
    smtp.quit()
   
    print(f"Sending e-mail from {remitente} to {destinatario} with the subject: {asunto}")
    print(f"Body e-mail (HTML):\n{cuerpo_html}")


    return True
  except Exception as e:
    print(f"Error sending email: {e}")
    return False