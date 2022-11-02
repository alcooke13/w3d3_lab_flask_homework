from app import app

@app.route('/')
def index():
    return "Hellow World"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"
    