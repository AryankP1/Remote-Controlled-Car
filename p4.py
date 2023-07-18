from microbit import *
import radio
radio_channel = 5
radio.config(group=radio_channel)
radio.on()
speed = 0
clock = True
while True:
    clock = True
    if button_a.is_pressed():
        radio.send('stop')
    if button_b.is_pressed():
        radio.send('go')
    xpos, ypos, zpos = accelerometer.get_values()
    if (xpos > 300 and ypos > 200):
        display.show(Image.ARROW_SE)
        print("Good")
    elif (xpos < -300 and ypos > 500):
        display.show(Image.ARROW_SW)
    elif (xpos > 300 and ypos < -400):
        display.show(Image.ARROW_NE)
    elif (xpos < -300 and ypos < -400):
        display.show(Image.ARROW_NW)
    elif (ypos > 600):
        display.show(Image.ARROW_S)
    elif (ypos < -300):
        display.show(Image.ARROW_N)
    elif (xpos > 300):
        display.show(Image.ARROW_E)
    elif (xpos < -300):
        display.show(Image.ARROW_W)
    if button_a.is_pressed():
        Speed = 500
    if button_b.is_pressed():
        Speed = 200
