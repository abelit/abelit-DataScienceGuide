from flask import Flask, jsonify, request, Blueprint
from flask_sockets import Sockets
import datetime
import time
import random
from queue import Queue 

app = Flask(__name__)
sockets = Sockets(app)
datas_queue = Queue(maxsize=50)
datas_queue.put(250)

@sockets.route('/echo')
def echo_socket(ws):
    output_datas = []
    while not ws.closed:
        if datas_queue.empty() or datas_queue.qsize() < 10:
            now = datetime.datetime.now().isoformat() + 'Z'
            ws.send(now)  #发送数据
            time.sleep(1)
            # datas_queue.put("正在更新数据")
            # ws.send(datas_queue.get())
        else:
            if not datas_queue.empty():
                output_datas.append(datas_queue.get()) 
            ws.send(output_datas)
            time.sleep(2)

datas = Blueprint("data", __name__, url_prefix="/api")
# app.register_blueprint(datas)
@datas.route("/connect", methods=["GET", "POST"])
def connect():
    return jsonify({"infos":"connecting succeessfully"})

@datas.route('/data/put-queue', methods=["GET", "POST"])
def put_queue():
    put_datas = request.json["put_datas"]
    datas_queue.put(put_datas)
    datas_number = datas_queue.qsize()
    return jsonify({"input_datas":put_datas, "datas_number":datas_number})

@datas.route("/data/get-queue", methods=["GET", "POST"])
def get_queue():
    # get_datas = request.json["get_datas"]
    if datas_queue.empty():
        datas_queue.put("队列数消费完,请重新添加数据")
        output_datas = datas_queue.get()
        return jsonify({"output_datas":output_datas})
    else:
        output_datas = datas_queue.get()
        datas_left_number = datas_queue.qsize()
        return jsonify({"output_datas":output_datas, "datas_left_nubmer":datas_left_number})

if __name__ == "__main__":
    app.register_blueprint(datas)
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from gevent import monkey
    monkey.patch_all()
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()