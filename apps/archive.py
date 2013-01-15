from apps import app

@app.route('/')
def hello():
    return "hello world"
