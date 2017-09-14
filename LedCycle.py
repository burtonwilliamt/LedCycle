from gpiozero import LED
from time import sleep

light1 = [LED(26),LED(19),LED(13)]
light2 = [LED(16),LED(20),LED(21)]
light3 = [LED(25),LED(7),LED(12)]
light4 = [LED(24),LED(23),LED(18)]
light5 = [LED(6),LED(5),LED(22)]
light6 = [LED(27),LED(17),LED(4)]

lights = [light1, light2, light3, light4, light5, light6]

red = [0.5,0.0,0.0]
green = [0.0,1.0,0.0]
blue = [0.0,0.0,1.0]

yellow = [0.5,1.0,0.0]
teal = [0.0,1.0,1.0]
purple = [0.5,0.0,1.0]

colors = [red,green,blue,yellow,teal,purple]

cycleTime = 3000

def checkColor(l, c, i):
	if(i < c[0]):
		l[0].off()
	else:
		l[0].on()
	if(i < c[1]):
		l[1].off()
	else:
		l[1].on()
	if(i < c[2]):
		l[2].off()
	else:
		l[2].on()
	
while True:
	for i in range(len(colors)):
		for k in range(cycleTime):
			count = 0.0
			while count < 1.0:
				for j in range(len(lights)):
					checkColor(lights[j], colors[(j+i)%len(colors)], count)
				count += 0.1

