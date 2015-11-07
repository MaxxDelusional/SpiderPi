import sys,tty,termios
import RPi.GPIO as GPIO

LEFT_PIN = 26
RIGHT_PIN = 16

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def forward():
    GPIO.output(LEFT_PIN, True)
    GPIO.output(RIGHT_PIN, True)

def left():
    GPIO.output(LEFT_PIN, True)
    GPIO.output(RIGHT_PIN, False)

def right():
    GPIO.output(LEFT_PIN, False)
    GPIO.output(RIGHT_PIN, True)

def stop():
    GPIO.output(LEFT_PIN, False)
    GPIO.output(RIGHT_PIN, False)

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break

    if k == 'w':
        forward()
    elif k == 'a':
        left()
    elif k == 'd':
        right()
    elif k == 's':
        stop()
    else:
        return False

    return True

def main():
    print "Hello Spider"
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    while get():
        print "Still Running"

    print "Exiting"
    GPIO.cleanup()

if __name__=='__main__':
        main()
