# John Mihal
# jm7198@rit.edu
# RIT Racing

import tkinter as tk
import RPi.GPIO as GPIO
import time


def adjust_voltage(val):
    print(val)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    print('voltage high')
    time.sleep(5)

    GPIO.cleanup()
    print('cleaned up')

def main():
    root = tk.Tk()
    
    message = tk.Label(root, text="Slide to Adjust Voltage")
    message.pack()
    
    message = tk.Label(root, text="0")
    message.pack()
    
    slider = tk.Scale(root, from_=0, to=5, command=adjust_voltage)
    slider.pack()
    
    message = tk.Label(root, text="5")
    message.pack()
        
    root.mainloop()


if __name__ == '__main__':
    main()