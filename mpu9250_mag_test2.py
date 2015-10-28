#!usr/bin/env python

import mraa as m
import time

# Register addr.
MPUREG_I2C_SLV0_ADDR		= 0x25
MPUREG_USER_CTRL        	= 0x6A
MPUREG_I2C_MST_CTRL		= 0x24
MPUREG_I2C_SLV0_REG		= 0x26
MPUREG_I2C_SLV0_DO		= 0x63
MPUREG_I2C_SLV0_CTRL		= 0x27
MPUREG_EXT_SENS_DATA_00		= 0x49
MPUREG_PWR_MGMT_1		= 0x6B
MPUREG_PWR_MGMT_2		= 0x6C
MPUREG_INT_PIN_CFG		= 0x37
MPUREG_I2C_MST_DELAY_CTRL 	= 0x67

AK8963_WIA			= 0x00
AK8963_CNTL1			= 0x0A
AK8963_CNTL2			= 0x0B
AK8963_HXL			= 0x03
AK8963_I2C_ADDR         	= 0x80


def mpu9250_writeReg(address, value):
        spi.write_word(((address & 0x7F) << 8) | (value & 0xFF));
        return;

def mpu9250_readReg(address):
	data = spi.write_word(((address & 0x7F) << 8) | 0x8000);
	return data;

spi = m.Spi(0);
spi.mode(m.SPI_MODE3);
spi.frequency(800000);
spi.bitPerWord(16);

mpu9250_writeReg(0x24, 0x40);
mpu9250_writeReg(0x25, 0x8C);
mpu9250_writeReg(0x26, 0x02);
mpu9250_writeReg(0x27, 0x88);
mpu9250_writeReg(0x28, 0x0C);
mpu9250_writeReg(0x29, 0x0A);
mpu9250_writeReg(0x2A, 0x81);
mpu9250_writeReg(0x64, 0x01);
mpu9250_writeReg(0x67, 0x03);
mpu9250_writeReg(0x01, 0x80);

mpu9250_writeReg(0x34, 0x04);
mpu9250_writeReg(0x64, 0x00);
mpu9250_writeReg(0x6A, 0x00);
mpu9250_writeReg(0x64, 0x01);
mpu9250_writeReg(0x6A, 0x20);
mpu9250_writeReg(0x34, 0x13);


rxbuff = mpu9250_readReg(0x36);
print "I2C Status 4 %#02x" % (rxbuff & 0x00FF)

for i in range(0,3):
	time.sleep(0.01)
	try:
		#rxbuff = spi.write_word(0x3F00 | 0x8000)
		#rxbuff = mpu9259_readReg(0x3F);
		rxbuff = mpu9250_readReg(0x4A);
		raw_input("%#02x" % (MPUREG_EXT_SENS_DATA_00+i));
		# print str(n)
                print "%#02x" % (rxbuff & 0x00FF)

	except:
		print("Error")	
			
