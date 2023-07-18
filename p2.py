# Write your code here :-)
from microbit import *
import radio
radio_channel = 5
radio.config(group=radio_channel)
radio.on()
trig = pin0
echo = pin1

motor_right = pin14
motor_rightDir = pin13
motor_left = pin16
motor_leftDir = pin15
speed = 0
motor_left.set_analog_period(1)
motor_right.set_analog_period(1)
motor_left.write_analog(1000)
motor_right.write_analog(1000)
clockwise = 0
anti_clockwise = 1
while True:
    display.show(Image.HAPPY)
    s = radio.receive()
    if s == 'stop':
        display.clear()
        break
while True:
    s = radio.receive()
    if s == 'stop':
        speed = 1000
    elif s == 'go':
        speed = 800
    motor_left.write_analog(speed)
    motor_right.write_analog(speed)
    dir = radio.receive()
    if dir == 'SE':
        motor_left.write_analog(speed-200)
        motor_right.write_analog(speed)
        motor_rightDir.write_digital(anti_clockwise)
        motor_leftDir.write_digital(anti_clockwise)
    elif dir == 'SW':
        motor_left.write_analog(speed)
        motor_right.write_analog(speed-200)
        motor_rightDir.write_digital(anti_clockwise)
        motor_leftDir.write_digital(anti_clockwise)
    elif dir == 'NE':
        motor_left.write_analog(speed-200)
        motor_right.write_analog(speed)
        motor_rightDir.write_digital(clockwise)
        motor_leftDir.write_digital(clockwise)
    elif dir == 'NW':
        motor_left.write_analog(speed)
        motor_right.write_analog(speed-200)
        motor_rightDir.write_digital(clockwise)
        motor_leftDir.write_digital(clockwise)
    elif dir == 'S':
        motor_leftDir.write_digital(anti_clockwise)
        motor_rightDir.write_digital(anti_clockwise)
    elif s == 'N':
        motor_leftDir.write_digital(clockwise)
        motor_rightDir.write_digital(clockwise)
    elif s == 'E':
        motor_rightDir.write_digital(anti_clockwise)
        motor_leftDir.write_digital(clockwise)
    elif s == 'W':
        motor_rightDir.write_digital(clockwise)
        motor_leftDir.write_digital(anti_clockwise)


