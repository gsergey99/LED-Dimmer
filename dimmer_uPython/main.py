# main.py -- put your code here!
############################################################
#   Project: LED-Dimmer 
#
#   Program name: main.py
#
#   Author: Sergio Jiménez
#
#   Date: 07-06-2020
#
#   Porpuse: Función de un LED-Dimmer
#
#   Revision History: Reflejado en el repositorio de GitHub
############################################################

from machine import Pin
from machine import ADC
from pyb import Timer
from pyb import ADC
from time import sleep
import machine
import time
import sys
import pyb

class LED_Dimmer():
    
    def __init__(self):
        """[Definición de atributos]
        """
        self.pin_rotary = pyb.Pin('PA1',pyb.Pin.IN)
        self.pin_led = pyb.Pin('PA5', pyb.Pin.OUT)
        self.rotary_angle = pyb.ADC(self.pin_rotary)
        self.led_timer = Timer(2, freq=100)
        self.led_pwm = self.led_timer.channel(1, Timer.PWM, pin=self.pin_led, pulse_width=0)
        self.timer_adc = None
        self.value_rotary = 0
    
    def callback_rotary(self,object):
        """[Definición del callback de la interrupción del timer]

        Arguments:
            object -- [Objeto timer_adc por argumento]
        """
        print(self.rotary_angle.read())
        self.value_rotary = self.rotary_angle.read()*48

    def start(self):
        """[Esta función inicia el timer para la captura de nuestro rotary angle sensor]
        """
        self.timer_adc = pyb.Timer(5,freq=100,period=99,prescaler=1,callback=self.callback_rotary)
        self.timer_adc.init(freq=100,period=99,prescaler=1)

next_state = 0

def initial_state(led_dimmer):

    led_dimmer.start()
    global next_state
    next_state = 1
    
def change_angle(led_dimmer):

    led_dimmer.led_pwm.pulse_width(led_dimmer.value_rotary)
    global next_state
    next_state = 1

print("*************LED-DIMMER*************")
led_dimmer = LED_Dimmer()
states = {0:initial_state,1:change_angle} 
value_rotary = 0

while True:
    try:
        
        states[next_state](led_dimmer)
    
    except Exception as ex:
        print("Any problem appears! Bye")
        sys.exit(0)
