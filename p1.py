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
        if pin_logo.is_touched():
            radio.send('faster')
    xpos, ypos, zpos = accelerometer.get_values()
    if (xpos > 300 and ypos > 200):
        display.show(Image.ARROW_SE)
        radio.send('SE')
    elif (xpos < -300 and ypos > 500):
        display.show(Image.ARROW_SW)
        radio.send('SW')
    elif (xpos > 300 and ypos < -400):
        display.show(Image.ARROW_NE)
        radio.send('NE')
    elif (xpos < -300 and ypos < -400):
        display.show(Image.ARROW_NW)
        radio.send('NW')
    elif (ypos > 600):
        display.show(Image.ARROW_S)
        radio.send('S')
    elif (ypos < -300):
        display.show(Image.ARROW_N)
        radio.send('N')
    elif (xpos > 300):
        display.show(Image.ARROW_E)
        radio.send('E')
    elif (xpos < -300):
        display.show(Image.ARROW_W)
        radio.send('W')
