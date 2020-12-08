import json
from flask import Flask, render_template, request
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

ws_pool = []


#  ws://
@sockets.route('/echo')
def echo_socket(ws):
    r_data = ws.receive()
    r_data = json.loads(r_data)
    if not r_data['type']=='open':
        return
    name = r_data['data']['name']
    for e in ws_pool:
        try:
            e.send(json.dumps({'type': 'enter', 'data':{'name':name}}))
        except:
            ws_pool.remove(e)

    ws_pool.append(ws)

    while not ws.closed:
        r_data = ws.receive()
        print(r_data)
        if r_data is None:
            break
        # ws.send("客户端已收到: " + str(message))
        # 如何推送给其他人
        r_data = json.loads(r_data)
        if r_data['type'] == 'say':
            data = r_data['data']
            for e in ws_pool:
                if e == ws:
                    continue
                e.send(json.dumps({'type': 'say', 'data':{'name': name, 'content': data['content']}}))

    ws_pool.remove(ws)
    for e in ws_pool:
        e.send(json.dumps({'type': 'leave', 'data':{'name': name}}))


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('0.0.0.0', 5002), app, handler_class=WebSocketHandler)
    print('web server start ... ')
    server.serve_forever()
