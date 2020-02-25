from flask import Flask
from flask_restplus import Api, Resource
import socket    
import requests
import psutil
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
API=Api(app)
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    request=requests.get(r'http://localhost:5000/conecta')
    print(request.json())

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
scheduler.start()
 
atexit.register(lambda: scheduler.shutdown())

@API.route('/conecta')
class Conecta(Resource):
    def get(self):
        cpu=psutil.cpu_percent()
        memory=dict(psutil.virtual_memory()._asdict()) 
        return{'cpu':cpu, 'memória total':memory['total'], 'memória disponível':memory['available'],'memória porcentagem':memory['percent'],'memória usada':memory['used'],
        }, 200
        #{'Allow-cross-origin-requests':'*'}



 
if __name__ == '__main__':
    app.run()