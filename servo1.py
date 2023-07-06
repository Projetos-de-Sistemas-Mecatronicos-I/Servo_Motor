# Import libraries
import RPi.GPIO as GPIO
import time

#cria variavel pino, a qual diz qual servo queremos q seja movido
#pino11 == servo1
#pino13 == servo2
#pino15 == servo3
pino = int(input())

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#função responsável por mover o servo selecionado pelo argumento "pino"
def move(pino):
    # Set pin 11 as an output, and define as servo1 as PWM pin
    GPIO.setup(pino,GPIO.OUT)
    servo1 = GPIO.PWM(pino,50) # pin 11 for servo1, pulse 50Hz

    # Start PWM running, with value of 0 (pulse off)
    servo1.start(0)

    # Loop to allow user to set servo angle. Try/finally allows exit
    # with execution of servo.stop and GPIO cleanup :)

    angle = float(0)
    servo1.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)

    angle = float(100)
    servo1.ChangeDutyCycle(2+angle/18)
    time.sleep(0.5)

    angle = float(0)
    servo1.ChangeDutyCycle(2+angle/18)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

    servo1.stop()
    GPIO.cleanup()

    return(print("This servo is enable"))

if pino==11:
    move(pino)
    print("The function Move runs!")

elif pino==13:
    move(pino)
    print("The function Move runs!")

elif pino==15:
    move(pino)
    print("The function Move runs!")

print("It's over")
