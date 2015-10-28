import mraa
import time

print(mraa.getPlatformName())

x = mraa.Gpio(69)
x.dir(mraa.DIR_OUT)

while True:
	x.write(1)
	time.sleep(1)
	x.write(0)
	time.sleep(1)
