from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    puppies=["fluffy", "Travis", "charlie"]
    return render_template('basic.html', puppies=puppies)

if __name__ == '__main__':
    app.run(debug=True)