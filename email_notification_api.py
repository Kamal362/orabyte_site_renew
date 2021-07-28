from flask import Flask
from flask_mail import Mail, Message

app_mail = Flask(__name__)

app_mail.config['MAIL_SERVER']='mail.orabytegh.com'
app_mail.config['MAIL_PORT']=26
app_mail.config['MAIL_USERNAME']="service@orabytegh.com"
app_mail.config['MAIL_PASSWORD']='orabyte3mail'
app_mail.config['MAIL_USE_SSL']=False
app_mail.config['MAIL_USE_TLS']=False


mail = Mail(app_mail)


def send_admins_mail(adm_mail,client_name):
    title = "Orabyte - Cliant Request"
    msg = "Dear developer, you are been notify by "+client_name+" who needs team orabyte service. Kindly reply using this "+adm_mail +" email provided. Thank you."
    message = Message(title, sender="service@orabytegh.com", recipients=['turntabl80@gmail.com','donklenam2@gmail.com','forsonimma1@gmail.com','charleskp138@gmail.com'])
    message.body = msg
    return mail.send(message)
    
  

def send_client_mail(cliant_email):
    subject = "Team Orabyte Service"
    msg = "Thank you for contacting team Orabyte, our team representative will be with you shortly."
    message = Message(subject, sender="service@orabytegh.com", recipients=[cliant_email])
    message.body = msg
    return mail.send(message)
      

# send_admins_mail('turntabl80@gmail.com','Gyan')
# send_client_mail('kamalissaw@gmail.com')

# if __name__ ==  '__main__':
#      app_mail.run(debug = True, host= '0.0.0.0')
