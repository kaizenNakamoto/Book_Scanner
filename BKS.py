import RPi.GPIO as G
import time
G.setwarnings(False)
G.cleanup()
G.setmode(G.BOARD)
G.setup(12,G.OUT)#in1
G.setup(32,G.OUT)#in2
G.setup(33,G.OUT)#in3
G.setup(35,G.OUT)#in4
G.setup(3,G.OUT)
G.setup(5,G.OUT)
mot1a=G.PWM(12,100)
mot1b=G.PWM(32,100)
mot2a=G.PWM(35,100)
mot2b=G.PWM(33,100)

def pg_rot(cc):
    if(cc==2):#counter clockwise
         mot1a.start(10)
         mot1b.start(0)
    elif cc==1:
         mot1a.start(0)
         mot1b.start(10)
    else:
        mot1a.start(0)
        mot1b.start(0)
def arm_rot(cc):
    if(cc==1):#counter clockwise
         mot2a.start(10)
         mot2b.start(0)
    elif cc==2:
         mot2a.start(0)
         mot2b.start(10)
    else:
        mot2a.start(0)
        mot2b.start(0)
def pull(cmd):
    if cmd==1:
        G.output(3,G.HIGH)
        G.output(5,G.LOW)
    else:
        G.output(3,G.LOW)
        G.output(5,G.LOW)
pull(1)
try:
    while(1):
        arm_rot(1)
        time.sleep(2)
        arm_rot(0)
        time.sleep(1)
        arm_rot(2)
        time.sleep(2)
        arm_rot(0)
        time.sleep(1)

except KeyboardInterrupt:
        print('out')
G.cleanup()
