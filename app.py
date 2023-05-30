from flask import Flask
#from flaskr import auth, blog

app = Flask(__name__)

#app.register_blueprint(auth.bp)
#app.register_blueprint(blog.bp)

@app.route('/')
def helloo():
    return 'Hello, World Externo!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
