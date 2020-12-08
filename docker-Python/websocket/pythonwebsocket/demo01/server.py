from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import *
    
app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*')

@app.route('/')
def index():
    return "hello abelit"

@socketio.on('gotit',namespace='/echo')
def test_message(message):
    print(message)
    emit('gotres', {'data': 'got it from backend!'})

# 连接事件
@socketio.on('connect', namespace='/echo')
def connect():
    # 函数名在内核事件中没有要求，只要不和关键字重复
    # if session['username'] == 'chenyang':
    #     print('您好！连接成功')
    #     emit('response', {'data': '您好！连接成功'})
    # else:
    #     disconnect()
    print('您好！连接成功')

# 断开连接事件
@socketio.on('disconnect', namespace='/echo')
def disconnect():
    print('有人断开连接')

@socketio.on('channel1', namespace='/echo')
def channel(message):
    #广播：当发送函数中指定了broadcast=True，那么所有连接到此服务器的客户端都会受到服务端发送的消息。
    emit('response', {'data': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)