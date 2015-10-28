#!usr/bin/env python

import mraa as m
import time

# Register addr.
MPUREG_I2C_SLV0_ADDR	= 0x25
MPUREG_USER_CTRL        = 0x6A
MPUREG_I2C_MST_CTRL	= 0x24
MPUREG_I2C_SLV0_REG	= 0x26
MPUREG_I2C_SLV0_DO	= 0x63
MPUREG_I2C_SLV0_CTRL	= 0x27
MPUREG_EXT_SENS_DATA_00	= 0x49
MPUREG_PWR_MGMT_1	= 0x6B
MPUREG_PWR_MGMT_2	= 0x6C
MPUREG_INT_PIN_CFG	= 0x37

AK8963_WIA		= 0x00
AK8963_CNTL1		= 0x0A
AK8963_CNTL2		= 0x0B
AK8963_HXL		= 0x03
AK8963_I2C_ADDR         = 0x7A


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


mpu9250_writeReg(MPUREG_PWR_MGMT_1, 0x80);
time.sleep(0.01)
mpu9250_writeReg(MPUREG_PWR_MGMT_1, 0x01);
time.sleep(0.001);
mpu9250_writeReg(MPUREG_PWR_MGMT_2, 0x00);
time.sleep(0.001);
#mpu9250_writeReg(MPUREG_INT_PIN_CFG, 0x30);
#time.sleep(0.001);

rxbuff = mpu9250_readReg(0x36);
print "I2C Status 1 %#02x" % (rxbuff & 0x00FF)

mpu9250_writeReg(MPUREG_USER_CTRL, 0x02);			# I2C Master Reset
time.sleep(0.1);
mpu9250_writeReg(MPUREG_USER_CTRL, 0x20);       		# I2C Master mode 
#raw_input("%#02x : 0x20" % MPUREG_USER_CTRL);
time.sleep(0.001);
mpu9250_writeReg(MPUREG_I2C_MST_CTRL, 0x0D);			# I2C multi-master IIC 400KHz
time.sleep(0.001);
mpu9250_writeReg(MPUREG_I2C_SLV0_ADDR, AK8963_I2C_ADDR); 	# I2C_SLAVE0_ADDR
#raw_input("%#02x : %#02x" % (MPUREG_I2C_SLV0_ADDR, AK8963_I2C_ADDR));
time.sleep(0.001);
rxbuff = mpu9250_readReg(MPUREG_I2C_SLV0_ADDR);
print "Slave address %#02x" % (rxbuff & 0x00FF)
raw_input("Nothing yet")

# Send RESET
mpu9250_writeReg(MPUREG_I2C_SLV0_REG, AK8963_CNTL2);
time.sleep(0.01);
mpu9250_writeReg(MPUREG_I2C_SLV0_DO, 0x01);
time.sleep(0.01);
mpu9250_writeReg(MPUREG_I2C_SLV0_CTRL, 0x81);
time.sleep(0.01);
rxbuff = mpu9250_readReg(0x36);
print "I2C Status 3 %#02x" % (rxbuff & 0x00FF)
raw_input("Reset sended");

# 16-bit output; continuous measurement mode 1
mpu9250_writeReg(MPUREG_I2C_SLV0_REG, AK8963_CNTL1);
time.sleep(0.001);
mpu9250_writeReg(MPUREG_I2C_SLV0_DO, 0x12);
time.sleep(0.001);
mpu9250_writeReg(MPUREG_I2C_SLV0_CTRL, 0x81);
time.sleep(0.001);

rxbuff = mpu9250_readReg(0x36);
print "I2C Status 4 %#02x" % (rxbuff & 0x00FF)

for i in range(0,3):
	time.sleep(0.01)
	try:
		#rxbuff = spi.write_word(0x3F00 | 0x8000)
		#rxbuff = mpu9259_readReg(0x3F);
		mpu9250_writeReg(MPUREG_I2C_SLV0_ADDR, AK8963_I2C_ADDR | 0x80);
		raw_input("...")
		time.sleep(0.001);
		mpu9250_writeReg(MPUREG_I2C_SLV0_REG, AK8963_WIA);
		time.sleep(0.001);
		raw_input("...")
		mpu9250_writeReg(MPUREG_I2C_SLV0_CTRL, 0x81);
		time.sleep(0.001);
		raw_input("...");
		rxbuff = mpu9250_readReg(MPUREG_EXT_SENS_DATA_00);
		raw_input("%#02x" % (MPUREG_EXT_SENS_DATA_00+i));
		# print str(n)
                print "%#02x" % (rxbuff & 0x00FF)

	except:
		print("Error")	
			
