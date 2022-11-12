# AC - artificial consiousness

import msvcrt
import time
import sys

class Memory:
    def __init__(self) -> None:
        self._memory = []  # the list of events. Simple liniar model of memory. sdf
        self._sum = ""


# main loop
# only inside loop AC can exist
def nastroenie():
    print("I'm born")
    mem = Memory()
    while True:   # Main live loop
         # --- function that saves input to then replay it ---
        if msvcrt.kbhit(): 
            key = msvcrt.getch()
            while not key.hex()=="0d":      # press enter to same the phrase
                print(key.decode(), end='', flush=True)  # print each entered key
                mem._sum += key.decode()
                key = msvcrt.getch()
        print(mem._sum)
        # ----
        # time.sleep(1)
        if mem._sum=="die":
            break


if __name__=="__main__":

    nastroenie()
    # print(key, end="")