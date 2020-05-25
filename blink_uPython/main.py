# main.py -- put your code here!

from machine import Pin
from machine import ADC
from pyb import Timer
from time import sleep

import time


def callback_rotary(value):
    print("Funcionando")

def callback_led(value):
    print("El valor es: ")

pin_rotary = Pin('PA1',Pin.IN)
pin_rotary.irq(handler= callback_rotary,trigger=Pin.IRQ_RISING)
rotary_angle = ADC(pin_rotary)


max_width = 200000
min_width = 20000

pin_led = pyb.Pin('PA5', pyb.Pin.OUT)


tim = pyb.Timer(2, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pin_led, pulse_width=0,callback=callback_led(rotary_angle))

print("*************LED-DIMMER*************")



while True:
    rotary_value = rotary_angle.read_u16()
    cur_width = rotary_value * 3 #Multiplicador para obtener más intensidad lumínica

    tchannel.pulse_width(cur_width)
    print(cur_width)
    sleep(0.01)


    """
    machine.lightsleep(100)
    #hola = pwm_led.value(1)
    value_rotary = rotary_angle.read_u16()
    intensity = value_rotary % 255
    #hola = pwm_led.value(intensity)
    print(intensity)
    machine.lightsleep(100)
    """
