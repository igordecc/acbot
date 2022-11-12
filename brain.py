# AC - artificial consiousness

import msvcrt
import time
import sys
import datetime

# temporal settings and preferences
# also called Mood, or Mood cycle, or Mood cycler
# point 2
class MoodHandler:  
    def __init__(self) -> None:
        self.birthday_time = time.time()
        self.mood = ""

    # define sleep or awake program right now
    # returns False if sleep and True if awake
    def sleep_wake_up_sleep(self):
        # every 10 seconds sleep
        sleep_phrase = "I am sleeping..."
        # every 10 seconds awake
        awake_phrase = "I am awake!"
        if round(time.time()%20) < 10:
            self.mood = sleep_phrase
            return False
        else:
            self.mood = awake_phrase
            return True

# point 3
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


# point 4
class Memory:
    def __init__(self) -> None:
        self._memory = []  # the list of events. Simple liniar model of memory. sdf
        self._event_sentence = ""


def output_memory(mem: Memory):
    if mem._memory:
            print(mem._memory[-1])

# main loop
# only inside loop AC can exist
def nastroenie():
    print("I'm born")
    mem = Memory()
    event_handler = EventHandler()
    mood_handler = MoodHandler()
    while True:   # Main live loop
        # --- function that saves input to then replay it ---
        event_handler.wait_and_memorise_an_event(mem)
        # returns are we wake up right now or in sleep mode
        # controlls waking up and put to sleep
        mood_handler.sleep_wake_up_sleep()  
        output_memory(mem)
        # ----
        # time.sleep(1)
        if mem._memory:
            if mem._memory[-1]=="die":
                break
        if mem._memory:
            if mem._memory[-1]=="how are you?":
                print(mood_handler.mood)


if __name__=="__main__":
    nastroenie()