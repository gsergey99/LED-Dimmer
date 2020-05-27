# main.py -- put your code here!

from machine import Pin
from machine import ADC
from pyb import Timer
from pyb import ADC
from time import sleep
import machine
import time
import sys

class LED_Dimmer():
    
    def __init__(self):
        """[Definición de atributos]
        """
        self.pin_rotary = pyb.Pin('PA1',pyb.Pin.IN)
        self.pin_led = pyb.Pin('PA5', pyb.Pin.OUT)
        self.rotary_angle = pyb.ADC(self.pin_rotary)
        self.led_timer = Timer(2, freq=100)
        self.led_pwm = self.led_timer.channel(1, Timer.PWM, pin=self.pin_led, pulse_width=0)
        self.timer_adc = pyb.Timer(5,freq=100,period=99,prescaler=1,callback=self.callback_rotary)
    
    def callback_rotary(self,object):
        """[Definición del callback de la interrupción del timer]

        Arguments:
            object -- [Objeto timer_adc por argumento]
        """

        print("Funcionando")
        print(self.rotary_angle.read())
        value_rotary = self.rotary_angle.read()*48
        self.led_pwm.pulse_width(value_rotary)

    def start(self):
        """[Esta función inicia el timer para la captura de nuestro rotary angle sensor]
        """
        self.timer_adc.init(freq=100,period=99,prescaler=1)

print("*************LED-DIMMER*************")
led_dimmer = LED_Dimmer()
led_dimmer.start()
while True:
    try:
        sleep(0.01)
    
    except Exception as ex:
        print("Any problem appears! Bye")
        sys.exit(0)
        