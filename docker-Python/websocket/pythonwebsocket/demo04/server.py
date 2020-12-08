# Copy of http://stackoverflow.com/a/20104705
from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = True

sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):
    print(ws)
    while True:
        message = ws.receive()
        ws.send(message[::-1])

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/client', methods=['GET'])
def echo_test():
    return render_template('client.html')

if __name__ == '__main__':
    app.run()