# Import required modules
import RPi.GPIO as GPIO # GPIO module to interact with the Raspberry Pi's pins
import time # time module to provide delay functionality

# Set servo motor pin, frequency, and duty cycles
servo_pin = 18  # set GPIO pin for servo motor. the hardware pwm pinouts are 13,19,12 and 18
freq = 50  # set frequency for servo motor
dc_initial = 2.5  # set initial duty cycle for servo motor
dc_fast = 7.5  # set duty cycle for fast movement
dc_limit = 12.5  # set duty cycle for limit range

# Set up GPIO mode and pin for output
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM object and start with initial duty cycle
pwm = GPIO.PWM(servo_pin, freq)
pwm.start(dc_initial)

try:
    # Move the servo motor quickly to limit range
    pwm.ChangeDutyCycle(dc_limit) # Change the duty cycle of the PWM signal to move the servo
    time.sleep(1) # Wait for 1 second

    # Move the servo motor back to 0 degrees
    pwm.ChangeDutyCycle(dc_initial) # Change the duty cycle of the PWM signal to move the servo
    time.sleep(1) # Wait for 1 second

except KeyboardInterrupt:
    # Cleanup GPIO settings when program is terminated
    pwm.stop()
    GPIO.cleanup() # Reset GPIO pins
