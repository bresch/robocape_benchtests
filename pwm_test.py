#!usr/bin/env python

import mraa as m
import time

pwm = m.Pwm(13)
pwm.period_us(700)
pwm.enable(True)
pwm.write(0.50)

while True:
	time.sleep(0.01)			
