from gpiozero import Button
from gpiozero import LED
button = Button(21)
green =LED(2)
yellow=LED(3)
while True:
	if button.is_pressed:
		green.on()
		yellow.off()
	else:
		green.off()
		yellow.on()
