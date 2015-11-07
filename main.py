import sys,tty,termios
import RPi.GPIO as GPIO

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break

        # print 'you pressed', ord(k)
        if k=='\x1b[A':
                print "up"
                GPIO.output(26, True)
        elif k=='\x1b[B':
                print "down"
                GPIO.output(26, False)
        elif k=='\x1b[C':
                print "right"
                GPIO.output(16, True)
        elif k=='\x1b[D':
                print "left"
                GPIO.output(16, False)
        else:
                print "not an arrow key!"

def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        
        while True:
                get()

if __name__=='__main__':
        main()
