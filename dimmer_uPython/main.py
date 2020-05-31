# main.py -- put your code here!
############################################################
#   Project: LED-Dimmer 
#
#   Program name: main.py
#
#   Author: Sergio Jiménez del Coso
#
#   Date: 07-06-2020
#
#   Porpuse: Función de un LED-Dimmer
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
        self.led_timer = pyb.Timer(2, freq=100)
        self.led_pwm = self.led_timer.channel(1, Timer.PWM, pin=self.pin_led, pulse_width=0)
        self.timer_adc = None
        self.value_rotary = 0
    
    def callback_rotary(self,timer):
        """[Definición del callback de la interrupción del timer, obtener valor del sensor]

        Arguments:
            timer -- [Objeto timer_adc por argumento]
        """
        self.value_rotary = self.rotary_angle.read()

    def start_timer(self):
        """[Esta función inicia el timer para la captura de nuestro rotary angle sensor]
        """
        self.timer_adc = pyb.Timer(5,freq=100,period=99,prescaler=1,callback=self.callback_rotary)
        self.timer_adc.init(freq=100,period=99,prescaler=1)

next_state = 0
value_bright = 0

def initial_state(led_dimmer):
    """[Función para definir el estado inicial]

    Arguments:
        led_dimmer -- [Objeto de led_dimmer por argumento]
    """
    led_dimmer.start_timer()
    global next_state
    next_state = 1
    
    
def measure_bright(led_dimmer):
    """[Función para definir el estado de cambio de intensidad del LED]

    Arguments:
        led_dimmer -- [Objeto de led_dimmer por argumento]
    """
    global next_state
    global value_bright

    value_bright = led_dimmer.value_rotary

    if value_bright < 15:
        value_bright = 0

    value_bright = value_bright * 36
    next_state = 2

def led_dimmed(led_dimmer):
    """[Función que modifica la señal que está asociacada al LED]

    Arguments:
        led_dimmer -- [Objeto de led_dimmer por argumento]]
    """
    global next_state
    
    led_dimmer.led_pwm.pulse_width(value_bright)
    next_state = 1

print("*************LED-DIMMER*************")
print("Please rotate the sensor")

states = {0:initial_state,1:measure_bright,2:led_dimmed} #definición de cada uno de los estados
led_dimmer = LED_Dimmer()

while True:
    try:
        
        states[next_state](led_dimmer) # cambio de estados
    except Exception as ex:
        print("Any problem appears! Bye")
        sys.exit(0)
