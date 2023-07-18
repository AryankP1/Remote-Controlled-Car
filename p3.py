# Write your code here :-)
from microbit import *
import radio
radio_channel = 5
radio.config(group=radio_channel)
radio.on()
motor_left = pin16
motor_leftDir = pin15
motor_right = pin14
motor_rightDir = pin13
Clockwise = 0
speed = 0
Anti_Clockwise = 1
motor_left.set_analog_period(1)
motor_right.set_analog_period(1)
motor_left.write_analog(1000)
motor_right.write_analog(1000)
while True:
    s = radio.receive()
    if s == 'stop':
        break
while True:
    s = radio.receive()
    if s == 'stop':
        speed = 1000
    elif s == 'go':
        speed = 800
    motor_left.write_analog(speed)
    motor_right.write_analog(speed)
