from threading import Timer
from time import time 
import os



def play2():
    print("works")
    os.system("exit")

timer = Timer(30, play2)
timer.start()




if __name__ == "__main__":
    print("start")
    print()

