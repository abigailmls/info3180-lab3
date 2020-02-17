from flask import Flask
from flask_mail import Mail 

app = Flask(__name__)
app.config['SECRET_KEY'] = '@bigail'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' 
app.config['MAIL_USERNAME'] = '8184435f92d65d'
app.config['MAIL_PASSWORD'] = 'c0822c86bceb99'

mail = MAIL(app)
from app import views