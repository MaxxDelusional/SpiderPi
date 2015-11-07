import sys,tty,termios,time
import RPi.GPIO as GPIO

LEFT_PIN = 26
RIGHT_PIN = 16
STATUS_PIN = 13

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
    time.sleep(0.1)
    GPIO.output(RIGHT_PIN, True)

def left():
    GPIO.output(LEFT_PIN, True)
    GPIO.output(RIGHT_PIN, False)

def right():
    GPIO.output(LEFT_PIN, False)
    GPIO.output(RIGHT_PIN, True)

def stop():
    GPIO.output((LEFT_PIN, RIGHT_PIN), False)

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
    elif k == 'p':
        return False

    return True

def main():
    print "Hello Spider"

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_PIN, GPIO.OUT)
    GPIO.setup(RIGHT_PIN, GPIO.OUT)
    GPIO.setup(STATUS_PIN, GPIO.OUT)

    GPIO.output(STATUS_PIN, True)
    while get():
        print "Still Running"

    print "Exiting"
    GPIO.output(STATUS_PIN, False)
    GPIO.cleanup()

if __name__=='__main__':
    main()
