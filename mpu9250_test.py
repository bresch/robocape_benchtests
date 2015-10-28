#!usr/bin/env python

import mraa as m
import time

spi = m.Spi(0)
spi.mode(m.SPI_MODE3)
spi.frequency(800000)
spi.bitPerWord(16)

while True:
	time.sleep(0.01)
	try:
		rxbuff = spi.write_word(0x3F00 | 0x8000)
		# print str(n)
                print "%#02x" % (rxbuff & 0x00FF)

	except:
		print("Error")	
			
