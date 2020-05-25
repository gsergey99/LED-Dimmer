# main.py -- put your code here!

from machine import Pin
from machine import ADC
from machine import Signal
from pyb import Timer
from time import sleep

import time
import math


def interruption_led(value):
    print("Encendido")

def irq_rotary(value):
    print("Funcionando")

max_width = 200000
min_width = 20000

pinout_led = pyb.Pin('PA5', pyb.Pin.OUT)

tim = pyb.Timer(2, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pinout_led, pulse_width=0,callback=interruption_led)

pin_rotary = Pin('PA1',Pin.IN)
pin_rotary.irq(handler= irq_rotary,trigger=Pin.IRQ_RISING)
rotary_angle = ADC(pin_rotary)


wstep = 1500
cur_width = min_width

while True:
    rotary_value = rotary_angle.read_u16()
    cur_width = rotary_value

    tchannel.pulse_width(cur_width)
    print(cur_width)
    sleep(0.01)

    cur_width += wstep

    if cur_width > max_width:
        cur_width = max_width
        wstep *= -1
    elif cur_width < min_width:
        cur_width = min_width
        wstep *= -1

    """
    machine.lightsleep(100)
    #hola = pwm_led.value(1)
    value_rotary = rotary_angle.read_u16()
    intensity = value_rotary % 255
    #hola = pwm_led.value(intensity)
    print(intensity)
    machine.lightsleep(100)
    """
