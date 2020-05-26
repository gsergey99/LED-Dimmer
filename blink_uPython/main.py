# main.py -- put your code here!

from machine import Pin
from machine import ADC
from pyb import Timer
from pyb import ADC
from time import sleep
import machine
import time

max_width = 200000
min_width = 20000
cur_width = 0



def callback_led(value):
    print("El valor es: ")
    print(value)


#DEFINIMOS ADC
pin_rotary = pyb.Pin('PA1',pyb.Pin.IN)
rotary_angle = pyb.ADC(pin_rotary)

#DEFINIMOS EL LED

pin_led = pyb.Pin('PA5', pyb.Pin.OUT)
tim = pyb.Timer(2, freq=100) #El 2 significa que estamos utilizando una señal PMW para el LED que está asociado
tchannel = tim.channel(1, Timer.PWM, pin=pin_led, pulse_width=0) #,callback=callback_led


#DEFINIMOS EL TIMER QUE SE UTILIZARÁ PARA LA INTERRUPCIÓN
timer_adc = pyb.Timer(5)
timer_adc.init(freq=100)

def callback_rotary(rotary_angle,channel):
    print("Funcionando")
    print(rotary_angle.read())
    value_rotary = rotary_angle.read() * 16
    channel.pulse_width(value_rotary)
    #timer_adc.callback(callback_rotary(rotary_angle,tchannel))

    

print("*************LED-DIMMER*************")
#timer_adc.init(freq=100)
#timer_adc.callback(callback_rotary(rotary_angle,tchannel))

while True:
    timer_adc.callback(callback_rotary(rotary_angle,tchannel))
    
    sleep(0.01)


    """
    machine.lightsleep(100)
    #hola = pwm_led.value(1)
    value_rotary = rotary_angle.read_u16()
    intensity = value_rotary % 255
    #hola = pwm_led.value(intensity)
    print(intensity)
    machine.lightsleep(100)
    #rotary_value = rotary_angle.read_u16()
    #rotary_value = rotary_angle.read()
    #cur_width = rotary_value * 16 #Multiplicador para obtener más intensidad lumínica

    #tchannel.pulse_width(cur_width)
    #print(cur_width)
    """

"""
pin_rotary = Pin('PA1',Pin.IN)
pin_rotary.irq(handler= callback_rotary,trigger=Pin.IRQ_RISING)
rotary_angle = ADC(pin_rotary)
"""