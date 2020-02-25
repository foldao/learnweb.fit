from flask import Flask
from flask_restplus import Api, Resource
import socket    
import requests
import psutil
import time
import atexit
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db=SQLAlchemy(app)
API=Api(app)
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    return app
class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(80), nullable=False)
    IP = db.Column(db.String(120), nullable=False)
    CPU= db.Column(db.String(120), nullable=False)
    Memoria_total=db.Column(db.String(120), nullable=False)
    Memoria_disp=db.Column(db.String(120), nullable=False)
    memoria_usada=db.Column(db.String(120), nullable=False)
    memoria_percnt=db.Column(db.String(120), nullable=False)
    time=db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<host %r>' % self.host

def insert_status(req):
    insert=Status(host=req['hostname'],IP=req['IP'], CPU=req['cpu'],memoria_percnt=req['memória porcentagem'], Memoria_total=req['memória total'],memoria_usada=req['memória usada'],Memoria_disp=req['memória disponível'], time=time.strftime("%A, %d. %B %Y %I:%M:%S %p") )
    db.session.add(insert)
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    request=requests.get(r'http://localhost:5000/conecta')
    print(request.json())
    insert_status(request.json())
    db.session.commit()
 
atexit.register(lambda: scheduler.shutdown())

@API.route('/conecta')
class Conecta(Resource):
    def get(self):
        cpu=psutil.cpu_percent()
        memory=dict(psutil.virtual_memory()._asdict()) 
        return{'hostname':hostname,'IP':IPAddr,'cpu':cpu, 'memória total':memory['total'], 'memória disponível':memory['available'],'memória porcentagem':memory['percent'],'memória usada':memory['used'],
        }, 200
        #{'Allow-cross-origin-requests':'*'}



 
if __name__ == '__main__':
    db.create_all()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=1)
    scheduler.start()
    app.run()