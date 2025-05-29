# utils/sensor_temp.py
import smbus2

MAX30205_ADDRESS = 0x48
TEMP_REGISTER = 0x00

bus = smbus2.SMBus(1)

def leer_temperatura_max30205():
    data = bus.read_i2c_block_data(MAX30205_ADDRESS, TEMP_REGISTER, 2)
    raw_temp = (data[0] << 8) | data[1]
    temp_c = raw_temp * 0.00390625
    return temp_c

def calcular_puntaje_temperatura(temp):
    if temp is None:
        return 0

    if 37.2 <= temp <= 37.7:
        return 5
    elif 37.8 <= temp <= 38.2:
        return 10
    elif 38.3 <= temp <= 38.8:
        return 15
    elif 38.9 <= temp <= 39.3:
        return 20
    elif 39.4 <= temp <= 39.9:
        return 25
    return 0
