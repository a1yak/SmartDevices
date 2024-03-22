import eventlet

from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

#import paho.mqtt.client as mqtt
import time

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'user12345'
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False


mqtt = Mqtt(app)
socketio = SocketIO(app)

#def connect_broker(broker_address, client_name):
#    client = mqtt.Client(client_name)
 #   client.connect(broker_address)
  #  time.sleep(1)
   # client.loop_start()
    #return client

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('temperature')  # Change to your desired topic

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)

@app.route('/')
def index():
    return render_template('index.html')

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

if __name__ == '__main__':
    server = "broker.hivemq.com"
    client_name = "lab3client"
    socketio.run(app, host='localhost', port=5000, use_reloader=True, debug=True)
  #  mqtt_client = connect_broker(server, client_name)
   # try:
    #except KeyboardInterrupt:
     #   mqtt_client.disconnect()
      #  mqtt_client.loop_stop()
