import paho.mqtt.client as mqtt
import time
from sense_hat import SenseHat

sense = SenseHat()

# set up mqtt client
client = mqtt.Client("python_pub")
broker = ""
topic = ""

#set server to publish to
client.connect(broker, 1883)
client.loop_start()

while True:
    temp = sense.get_temperature()
    temp = round(temp, 2)
    msg_temp = "T = %s" % (temp)

    sense.show_message(msg_temp)

    #publish temperature to topic
    client.publish(topic, msg_temp)

    #pause for 5 seconds
    time.sleep(5)

