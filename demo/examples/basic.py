from flask import Flask

app = Flask(__name__)

@app.route('/')  #http://127.0.0.1:5000/
def index():
    return "<h1>Hello Puppy!</h1>"


@app.route('/cute')  #http://127.0.0.1:5000/cute
def cute():
    return "<h1>Puppies are cute!</h1>"

@app.route('/profiles/<name>')  #http://127.0.0.1:5000/profiles/travis
def profile(name):
    return f"<h1>This is a page for {name}!</h1>"

if __name__ == '__main__':
    #app.run()
    app.run(debug-True)