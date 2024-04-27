from gpiozero import AngularServo
import time
import pyttsx3
from PiicoDev_LIS3DH import PiicoDev_LIS3DH #type:ignore
from PiicoDev_Unified import sleep_ms #type:ignore

def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

motion =  PiicoDev_LIS3DH()



class Movements():
    def Hanshake():
        pin_number1 = 7

        servo1 = AngularServo(pin_number1,min_pulse_width=0.0006,max_pulse_width=0.0023)

        servo1.angle=90
        servo1.angle=-90
        servo1.angle=90
        servo1.angle-90
        speak("Enough handshakes now lets talk some serious stuff")

    def FallLRF():
        x,y,z = motion.angle
        print("Angle: ".format(y))

        formatted_y = format(y)
        formatted_x = format(x)

        #if threshold +y :
            #InitialiseRight()
            #if get pressure at InitialiseRightJoint:
                #GetupRight()
        
        #if threshold -y :
            #InitialiseLeft()
            #if get pressure at InitialiseLeftJoint:
                #GetupLeft()
        
        #if threshold +x :
            #InitialiseFront
            #if get pressure at initialiseFrontJoint:
                #GetupFront()

        #if threshold -y:
            #InitialiseBack
            
            #if get pressure at InitialiseBackJoint:
                #GetupBack()

        sleep_ms(50)

    def Getshake(): #Runs in Loop
        if motion.shake(threshold=20):
            speak("Yoo dont shake me too much!")
        if motion.shake(threhsold=12):
            speak("It would be better if you dont shake me")
    