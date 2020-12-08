# from geventwebsocket.handler import WebSocketHandler
# from gevent.pywsgi import WSGIServer
# from flask import Flask, request, render_template_string
# from flask_sockets import Sockets
# import json

# app = Flask(__name__)
# sockets = Sockets(app)

# template = """
# <html><body><table>
# {% for key, value in appliances.iteritems() %}
# <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
# {% endfor %}
# </table>
# <form>
# <input type="text" id="device">
# <input type="number" id="capacity" step="1" pattern="\d*">
# <input type="submit">
# </form>
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
# <script type="text/javascript">
# $(function() {
#   var socket = new WebSocket("ws://" + document.domain + ":5000/api");
#   socket.onmessage = function(message) {
#     var data = JSON.parse(message.data);
#     $("table").append("<tr><td>" + data.device + "</td><td>" + data.capacity + "</td></tr>");
#   };
#   $("form").submit(function(event) {
#     var data = {"device" : $("#device").val(), "capacity" : parseInt($("#capacity").val(), 10)};
#     socket.send(JSON.stringify(data));
#     event.preventDefault();
#   });
# });
# </script>
# </body></html>
# """

# @app.route('/')
# def index():
#     with open('appliances.json', 'r') as json_file:
#         appliances = json.load(json_file)
#     return render_template_string(template, appliances=appliances)
    
# @sockets.route('/api')
# def api(socket):
#     while True:
#         message = socket.receive()
#         socket.send(message)
#         data = json.loads(message)
#         with open('appliances.json', 'r') as json_file:
#             appliances = json.load(json_file)
#         appliances[data['device']] = data['capacity']
#         with open('appliances.json', 'w') as json_file:
#             json.dump(appliances, json_file)

# if __name__ == '__main__':
#     http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
#     http_server.serve_forever()

from flask.ext.socketio import SocketIO, emit
from flask import Flask, render_template_string
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.config['DEBUG'] = True

template = """
<html><body><table>
{% for key, value in appliances.iteritems() %}
<tr><td>{{ key }}</td><td>{{ value }}</td></tr>
{% endfor %}
</table>
<form>
<input type="text" id="device">
<input type="number" id="capacity" step="1" pattern="\d*">
<input type="submit">
</form>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/0.9.16/socket.io.min.js"></script>
<script type="text/javascript">
$(function() {
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('update', function(message) {
    var data = JSON.parse(message);
    $("table").append("<tr><td>" + data.device + "</td><td>" + data.capacity + "</td></tr>");
  });
  $("form").submit(function(event) {
    var data = {"device" : $("#device").val(), "capacity" : parseInt($("#capacity").val(), 10)};
    socket.emit('update', JSON.stringify(data));
    event.preventDefault();
  });
});
</script>
</body></html>
"""

@app.route('/')
def index():
    with open('appliances.json', 'r') as json_file:
        appliances = json.load(json_file)
    return render_template_string(template, appliances=appliances)
    
@socketio.on('update')
def api(message):
    emit('update', message, broadcast=True)
    data = json.loads(message)
    with open('appliances.json', 'r') as json_file:
        appliances = json.load(json_file)
    appliances[data['device']] = data['capacity']
    with open('appliances.json', 'w') as json_file:
        json.dump(appliances, json_file)

if __name__ == '__main__':
    socketio.run(app)