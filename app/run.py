from flask import Flask, render_template, jsonify, session
from flask_restplus import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db=SQLAlchemy(app)
apis=Api(app)

CORS(app, resources={r'/*': {'origins': '*'}})

parser = reqparse.RequestParser()
user=parser.add_argument('user')
psw=parser.add_argument('psw')

@apis.route('/login')
class Login(Resource):
    @apis.expect(parser)
    def options(self):
          return 200
    @apis.expect(parser)
    def post(self):
        args = parser.parse_args()
        print(parser)
        user=args['user']
        psw=args['psw'] 
        print(user)
        print(psw)
        if psw=='55718789' and user=='foldao':
            session['user']=user
            return{ 'login': 'success' }, 200, {'Access-Control-Allow-Origin': '*'}
        else:
            return{ 'login': 'fail' }, 403, {'Access-Control-Allow-Origin': '*'}
    
def get_user():
        try: 
            usr=session['user']
        except:
            usr=False
        return usr


@apis.route('/logout')
class Logout(Resource):
    def options(self):
        return 200
    def delete(self):    
        if get_user():
            del session['user']
            return {'logout':'success'}, 200, {'Access-Control-Allow-Origin': '*'}
        else:
            return {'logout':'no session found'}, 404, {'Access-Control-Allow-Origin': '*'}
            
@apis.route('/user')
class User(Resource):

    def get(self):    
        if get_user():
            return {'user':get_user()}, 200, {'Access-Control-Allow-Origin': '*'}
        else:
            print('teste')
            return {'user':'no session found'}, 404, {'Access-Control-Allow-Origin': '*'}

@apis.route('/teste')
class main_page(Resource):
    def get(self):
        isActive='isActive'
        true='true'
        age='age'
        name='name'
        first='first'
        last='last'
        _rowVariant='_rowVariant'
        false='false'
        _cellVariants='_cellVariants'
        x= [{ isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
          { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },
          {
            isActive: false,
            age: 9,
            name: { first: 'Mini', last: 'Navarro' },
            _rowVariant: 'success'
          },
          { isActive: false, age: 89, name: { first: 'Geneva', last: 'Wilson' } },
          { isActive: true, age: 38, name: { first: 'Jami', last: 'Carney' } },
          { isActive: false, age: 27, name: { first: 'Essie', last: 'Dunlap' } },
          { isActive: true, age: 40, name: { first: 'Thor', last: 'Macdonald' } },
          {
            isActive: true,
            age: 87,
            name: { first: 'Larsen', last: 'Shaw' },
            _cellVariants: { age: 'danger', isActive: 'warning' }
          },
          { isActive: false, age: 26, name: { first: 'Mitzi', last: 'Navarro' } },
          { isActive: false, age: 22, name: { first: 'Genevieve', last: 'Wilson' } },
          { isActive: true, age: 38, name: { first: 'John', last: 'Carney' } },
          { isActive: false, age: 29, name: { first: 'Dick', last: 'Dunlap' }}]
        
        return {'type':x},200, {'Access-Control-Allow-Origin': '*'}
@app.route('/home')
def index():
    return render_template('SPA.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__': 
  app.secret_key='bean legalzao'
  app.run(host='127.0.0.1', port=5002, debug=True)  
 
             
