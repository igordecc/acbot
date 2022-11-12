# AC - artificial consiousness

import msvcrt
import time
import sys

class Memory:
    def __init__(self) -> None:
        self._memory = []  # the list of events. Simple liniar model of memory. sdf
        self._event_sentence = ""


class EventHandler:

    # saves input inside memory_instance
    def wait_and_memorise_an_event(self, memory_instance: Memory):
        if msvcrt.kbhit(): 
            key = msvcrt.getch()
            while not key.hex()=="0d":      # press enter to same the phrase
                print(key.decode(), end='', flush=True)  # print each entered key
                memory_instance._event_sentence += key.decode()
                key = msvcrt.getch()
            memory_instance._memory.append(memory_instance._event_sentence)
            memory_instance._event_sentence = ""


# main loop
# only inside loop AC can exist
def nastroenie():
    print("I'm born")
    mem = Memory()
    event_handler = EventHandler()
    while True:   # Main live loop
         # --- function that saves input to then replay it ---
        event_handler.wait_and_memorise_an_event(mem)
        if mem._memory:
            print(mem._memory[-1])
        # ----
        # time.sleep(1)
        if mem._event_sentence=="die":
            break


if __name__=="__main__":
    nastroenie()
    # print(key, end="")