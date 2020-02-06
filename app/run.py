from flask import Flask, render_template
from views.api import APIs
from flask_restplus import Api, Resource
app = Flask(__name__)

apis=Api(app)
@apis.route('/teste')
class main_page(Resource):
    def get(self):
        return {'status':'ok'}, 200
@app.route('/home')
def index():
    return render_template('SPA.html')

if __name__ == '__main__': 
  app.run(host='127.0.0.1', port=5000, debug=True)  
 
             
