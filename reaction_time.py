from gpiozero import Button
from gpiozero import LED
from time import *
import time
import random 

button = Button(21)
green =LED(2)
yellow=LED(3)


green.on()
yellow.off()

wait = random.randint(2,7)
sleep(wait)

start_time = time.time()

while True:
	if button.is_pressed:
		yellow.off()
		end_time = time.time()
		elapsed_time = end_time - start_time
		print ("You took " + "%.2f" %elapsed_time + " seconds")
		break
	else:
		yellow.on()
		green.off()

green.off()
yellow.off()
