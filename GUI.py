from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
GreenLed = LED(18)
RedLed = LED(17)
BlueLed = LED(22)

## Gui Definitions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event Functions
def ledToggleGreen():
	if GreenLed.is_lit:
		GreenLed.off()
		ledButtonGreen["text"] = "Turn Green LED on"
	else:
		GreenLed.on()
		ledButtonGreen["text"] = "Turn Green LED off"
def ledToggleRed():
	if RedLed.is_lit:
		RedLed.off()
		ledButtonRed["text"] = "Turn Red LED on"
	else:
		RedLed.on()
		ledButtonRed["text"] = "Turn Red LED off"
def ledToggleBlue():
	if BlueLed.is_lit:
		BlueLed.off()
		ledButtonBlue["text"] = "Turn Blue LED on"
	else:
		BlueLed.on()
		ledButtonBlue["text"] = "Turn Blue LED off"
def close():
	RPi.GPIO.cleanup()
	win.destroy()

## Widgets
print ("starting app")
ledButtonGreen = Button(win, text = 'Turn Green LED On', font = myFont, command = ledToggleGreen, bg = 'bisque2', height = 1, width = 25)
ledButtonGreen.grid(row=0, column=1)

ledButtonRed = Button(win, text = 'Turn Red LED On', font = myFont, command = ledToggleRed, bg = 'bisque2', height = 1, width = 25)
ledButtonRed.grid(row=0, column=2)

ledButtonBlue = Button(win, text = 'Turn Blue LED On', font = myFont, command = ledToggleBlue, bg = 'bisque2', height = 1, width = 25)
ledButtonBlue.grid(row=0, column=3)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'bisque2', height = 1, width = 25)
exitButton.grid(row=1, column=2)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
