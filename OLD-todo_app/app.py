#from flask import Flask

#from todo_app.flask_config import Config

#app = Flask(__name__)
#app.config.from_object(Config())


#@app.route('/')
#def index():
#    return 'Hello World! - Rajiv'

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
