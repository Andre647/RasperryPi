import machine
from machine import SPI, Pin
import time
import utime
from ili9341 import Display, color565


BOTAO_A = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
BOTAO_B = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
BOTAO_C = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)

A_last = time.ticks_ms()
B_last = time.ticks_ms()
C_last = time.ticks_ms()

spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14), width=320, height=240, rotation = 270)


def button_handler(pin):
    global A_last, B_last, C_last, BOTAO_A, BOTAO_B, BOTAO_C 
    if pin is BOTAO_A:
        if time.ticks_diff(time.ticks_ms(), A_last) > 500:
            display.clear()
            display.draw_image('emoji_triste2.raw', 35, 30, 255, 191)
          
    elif pin is BOTAO_B:
        if time.ticks_diff(time.ticks_ms(), B_last) > 500:
            display.clear()
            display.draw_image('emoji_susto.raw', 0, 0, 320, 240)

  
    elif pin is BOTAO_C:
        if time.ticks_diff(time.ticks_ms(), C_last) > 500:
            display.clear()
            display.draw_image('emoji_feliz4.raw', 40, 30, 250, 188)
            

BOTAO_A.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

BOTAO_B.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

BOTAO_C.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
