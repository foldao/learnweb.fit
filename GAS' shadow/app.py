from flask import Flask
from flask_restplus import Api, Resource
import socket    
import psutil

app = Flask(__name__)
API=Api(app)
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    



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