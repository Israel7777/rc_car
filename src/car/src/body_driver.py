#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String
ser = serial.Serial()
pub = rospy.Publisher('/sonar',String, queue_size = 2)
car_codes = {
	     	"a":"a",
			"b":"b",
			"c":"c",
			"d":"d",
			"e":"e",
			"f":"f",
			"g":"g",
			"h":"h",
			"i":"i",
			"j":"j",
			"k":"k",
			"l":"l",
			"m":"m",
			"n":"n",
			"o":"o",
			"p":"p",
			"q":"q"}

'''
Command             Byte    ASCII
Front Distance      97      a
Back Distance       98      b
Illumination        99      c
Forward             100     d
Backwards           101     e
Stop                102     f
Right               103     g
Left                104     h
No turning          105     i
Front LEDs ON       106     j
Front LEDs OFF      107     k
Brake LEDs ON       108     l
Brake LEDs OFF      109     m
Right Indicator ON  110     n
Right Indicator OFF 111     o
Left Indicator ON   112     p
Left Indicator OFF  113     q
'''
def serial_write(cmd):
	try:
		ser.write(cmd)
	except:
		if (ser.isOpen()):ser.close()
        if not(ser.isOpen()):
        	ser.open()
        	rospy.logerr("Error writing to serial port")

def callback_move(cmd):
    command = cmd.data
    if command in car_codes:
        print(car_codes[command])
        serial_write(car_codes[command])
        if command == 'a' or command == 'b':
        	sonar = ser.readline()
        	pub.publish(sonar)
        	print sonar
	
def init():
	rospy.init_node('body_node', anonymous=False)
	rospy.Subscriber('/command',String, callback_move)
	
	ser.baudrate = 9600
	ser.port = '/dev/rfcomm1'
	ser.timeout = 2
	ser.open()
	if not (ser.isOpen()):
		rospy.logerr("Error: Could not open bluetooth Serial Port")
	rospy.spin()
init()


