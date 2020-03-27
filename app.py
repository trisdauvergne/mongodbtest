from flask import Flask, render_template
import os
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

print(os.environ.get("SECRET_KEY"))
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def home():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',
    port=5000,
    debug=True)