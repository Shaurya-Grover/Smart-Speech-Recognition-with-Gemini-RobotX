from PiicoDev_LIS3DH import PiicoDev_LIS3DH #type:ignore
from PiicoDev_Unified import sleep_ms #type:ignore

motion =  PiicoDev_LIS3DH()

while True:
    x,y,z = motion.angle
    print("Angle: ".format(y))
    sleep_ms(50)