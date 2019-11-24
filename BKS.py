import RPi.GPIO as G
import time
G.setwarnings(False)
G.cleanup()
G.setmode(G.BOARD)
G.setup(5,G.OUT)
G.setup(33,G.OUT)
G.setup(35,G.OUT)
G.setup(3,G.OUT)
G.output(3,G.LOW)
G.output(5,G.LOW)
mot2=G.PWM(33,50) #arm
mot3=G.PWM(35,50) #page
mot2.start(0)
mot3.start(0)
def pg_rot(cc):
    if(cc==2):#counter clockwise
         mot3.ChangeDutyCycle(2.5)
    elif cc==1:
         mot3.ChangeDutyCycle(12.5)
    else:
         mot3.ChangeDutyCycle(0)
def arm_rot(ang):
    pwm=ang/18+2.5
    G.output(33,True)
    mot2.ChangeDutyCycle(pwm)
    time.sleep(0.3)
    G.output(33,False)
def pull(cmd):
    if cmd==1:
        G.output(3,G.HIGH)
        G.output(5,G.LOW)
    else:
        G.output(3,G.LOW)
        G.output(5,G.LOW)
pull(0)
count=0
time.sleep(3)
try:
    while(1):
        pull(1)
        arm_rot(max(18-(count*0.3),1))
        time.sleep(2)
        arm_rot(100)
        pg_rot(2)
        time.sleep(0.1)
        pull(0)
        time.sleep(0.5)
        pg_rot(0)
        time.sleep(0.2)
        pg_rot(1)
        time.sleep(0.6)
        pg_rot(0)
        time.sleep(0.3)
        count=count+1

except KeyboardInterrupt:
        print('out')
G.cleanup()
