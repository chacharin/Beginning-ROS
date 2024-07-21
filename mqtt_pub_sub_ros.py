#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, reason_code, properties):
    print("Connect with reason code:" + str(reason_code))

def on_message(mqttc, obj, msg):
    print(f"MSG from {msg.topic} : {msg.payload.decode('utf-8')}")
    value = msg.payload.decode('utf-8')
    pub.publish(value)
    rospy.loginfo(str(value))

def on_subscribe(mqttc, obj, mid, reason_code_list, properties):
    print(f"Subcribed: {mid}, Reson Code: {reason_code_list}")

def on_log(mqttc, obj, level, string):
    print(f"MQTT Log: {string}")
    
def sensor_callback(data):
    value = str(data.data)
    mqttc.publish("ros_sensor", value)
    rospy.loginfo("Value was Published to mqtt broker.")
    
mqttc =mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

mqttc.connect("o.tcp.ap.ngrok.io", 12631, 60)

rospy.init_node("mqtt_ros")
pub = rospy.Publisher("control", String, queue_size = 10)
sub = rospy.Subscriber("Topic_sensor", Int16, sensor_callback)

mqttc.loop_start()
rospy.spin()

mqttc.loop_stop()
mqtt.disconnect()
