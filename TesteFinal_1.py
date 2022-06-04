import machine
from machine import SPI, Pin
import time
import utime
from ili934xnew import ILI9341, color565
import tt32
from ili9341 import Display


BOTAO_A = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
BOTAO_B = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
BOTAO_C = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)

A_last = time.ticks_ms()
B_last = time.ticks_ms()
C_last = time.ticks_ms()
TFT_CLK_PIN = const(6)
TFT_MOSI_PIN = const(7) #SDOMOSI
TFT_MISO_PIN = const(4) #SDOMISO

TFT_CS_PIN = const(13)
TFT_RST_PIN = const(14)
TFT_DC_PIN = const(15)

SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(1)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14), width=320, height=240, rotation = 270)

# spi = SPI(
#     0,
#     baudrate=40000000,
#     miso=Pin(TFT_MISO_PIN),
#     mosi=Pin(TFT_MOSI_PIN)3,
#     sck=Pin(TFT_CLK_PIN))
#display1 = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))
# display = ILI9341(
#     spi,
#     cs=Pin(TFT_CS_PIN),
#     dc=Pin(TFT_DC_PIN),
#     rst=Pin(TFT_RST_PIN),
#     w=SCR_WIDTH,
#     h=SCR_HEIGHT,
#     r=SCR_ROT)

def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)
            
            
def draw_semi_circle_happy(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        #display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        #display.pixel(xpos0 - x, ypos0 + y, col)
        #display.pixel(xpos0 - x, ypos0 - y, col)
        #display.pixel(xpos0 - y, ypos0 - x, col)
        #display.pixel(xpos0 + y, ypos0 - x, col)
        #display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)
            
            

            
def draw_semi_circle_sad(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        #display.pixel(xpos0 + x, ypos0 + y, col)
        #display.pixel(xpos0 + y, ypos0 + x, col)
        #display.pixel(xpos0 - y, ypos0 + x, col)
        #display.pixel(xpos0 - x, ypos0 + y, col)
        #display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        #display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)



def button_handler(pin):
    global A_last, B_last, C_last, BOTAO_A, BOTAO_B, BOTAO_C
    time.sleep(1) 
    if pin is BOTAO_A:
        if time.ticks_diff(time.ticks_ms(), A_last) > 500:
            display.erase()
            display.set_font(tt32)
            display.set_color(color565(255, 255, 0), color565(0,0,0))
            
            i =  0
            while(i<10):
                draw_semi_circle_happy(CENTER_Y, CENTER_X - i, 100, color565(255, 255, 0))
                i = i + 1

            #display.set_color(color565(255,255,0), color565(0,0,0))
            display.set_pos(CENTER_Y-42,CENTER_X+30)
            #display.print("\___/")


            i =  0
            while(i<5):
                draw_circle(CENTER_Y+35, CENTER_X-50, 25 + i, color565(255, 255, 0))
                i = i +1
                
            display.set_pos(CENTER_Y+27,CENTER_X-62)
            display.print("o")

            
            i =  0
            while(i<5):
                draw_circle(CENTER_Y-35, CENTER_X -50,25 + i, color565(255, 255, 0))
                i = i +1
            display.set_pos(CENTER_Y-43,CENTER_X-62)
            display.print("o")
            
            display.set_pos(CENTER_Y-5,CENTER_X+20)
            display.print("V")
            
            #display.erase()
            #display1.draw_image('boredape2.raw', 0, 0, 224, 212)

          
    elif pin is BOTAO_B:
        if time.ticks_diff(time.ticks_ms(), B_last) > 500:
            display.erase()
            display.set_font(tt32)
            display.set_color(color565(255, 255, 0), color565(0,0,0))

            #draw_circle(CENTER_Y, CENTER_X, 100, color565(255, 255, 0))
    
            display.set_color(color565(255,255,0), color565(0,0,0))
            
            
            display.set_pos(CENTER_Y-40,CENTER_X+30)
            display.print("___")


            display.set_pos(CENTER_Y+30,CENTER_X-50)
            display.print("O")

            display.set_pos(CENTER_Y-50,CENTER_X-50)
            display.print("O")

  
    elif pin is BOTAO_C:
        if time.ticks_diff(time.ticks_ms(), C_last) > 500:
            display.erase()
            display.set_font(tt32)
            display.set_color(color565(255, 255, 0), color565(0,0,0))

            #draw_circle(CENTER_Y, CENTER_X, 100, color565(255, 255, 0))
        
            display.set_color(color565(255,255,0), color565(0,0,0))
            
            
            #display.set_pos(CENTER_Y-42,CENTER_X+30)
            #display.print("___")
            #display.set_pos(CENTER_Y-35,CENTER_X+20)
            #display.write("___\n             /       \\")
            i =  0
            while(i<10):
                draw_semi_circle_sad(CENTER_Y, CENTER_X + 170 - i, 100, color565(255, 255, 0))
                i = i + 1
            
            
            #draw_circle(CENTER_Y, CENTER_X, 100, color565(255, 255, 0))
            
            
            i =  0
            while(i<5):
                draw_circle(CENTER_Y+35, CENTER_X-50, 25 + i, color565(255, 255, 0))
                i = i +1
                
            display.set_pos(CENTER_Y+27,CENTER_X-62)
            display.print("o")

            
            i =  0
            while(i<5):
                draw_circle(CENTER_Y-35, CENTER_X -50,25 + i, color565(255, 255, 0))
                i = i +1
            display.set_pos(CENTER_Y-43,CENTER_X-62)
            display.print("o")
            
            display.set_pos(CENTER_Y-5,CENTER_X+10)
            display.print("V")


BOTAO_A.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

BOTAO_B.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

BOTAO_C.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
