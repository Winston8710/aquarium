import RPi.GPIO as GPIO
import time


trigger_pin = 23
echo_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True)

def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)
    
def Setup(GPIOnum, OUT_IN):
    GPIO.setmode(GPIO.BCM)
    
    if OUT_IN == "OUT" :
        GPIO.setup(GPIOnum, GPIO.OUT)
    else:
        GPIO.setup(GPIOnum, GPIO.IN)
def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)



def distance(speed=34300):
    send_trigger_pulse()
    while GPIO.input(echo_pin) == 0 :
        StartTime = time.time()
    while GPIO.input(echo_pin) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance_cm = (TimeElapsed * speed) / 2
    distance_in = distance_cm / 2.5
    return distance_cm
    
    
def distt():
    try:      
        while True:
            speed=34300
            dist = distance(speed)
            print ("Measured Distance = %.1f cm" % dist)
            time .sleep(1)
            if(dist<5): #觸發條件->距離小於5cm
                Setup(17, "OUT") #亮起左1紅色警示燈
                TurnOnLED(17)
                time.sleep(1)
                TurnOffLED(17)
                time.sleep(1) 
         
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup ()