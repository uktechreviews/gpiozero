from gpiozero import LED 
from signal import pause
green  = LED(2)
yellow = LED(3)
green.blink()
yellow.blink()
pause()
