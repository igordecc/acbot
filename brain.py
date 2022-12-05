# AC - artificial consiousness

import msvcrt
import time
import sys
import datetime

MOOD = ""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
# temporal settings and preferences
# also called Mood, or Mood cycle, or Mood cycler





def TematicMap():
    def __init__(self):
        self.sleep_state_1 = "I am sleeping..."
        self.sleep_state_2 = "I am awake!"

    

# point 2
class Mood(metaclass=Singleton):  
    def __init__(self) -> None:
        self.birthday_time = time.time()
        self.mood = ""

    # define sleep or awake program right now
    # returns False if sleep and True if awake
    def sleep_wake_up_sleep(self):
        global MOOD
        # every 10 seconds sleep
        sleep_phrase = "I am sleeping..."
        # every 10 seconds awake
        awake_phrase = "I am awake!"
        if round(time.time()%20) < 10:
            self.mood = sleep_phrase
            MOOD = sleep_phrase
            return False
        else:
            # self.mood = awake_phrase
            MOOD = awake_phrase
            return True


    # infinite cicle with list of things to repeat
    # ONE BIG CIRCLE
    def one_infinite_cicle(self, list_of_things_to_repeat: list):
        while True:
            for thing in list_of_things_to_repeat:
                thing()

    # main loop
    # only inside loop AC can exist
    # v1 only print mood based events
    def construct_mood_event_loop_and_boot_it(self):
        print("I'm born")
        mem = Memory()
        event_handler = EventHandler()
        mood_handler = Mood()
        reaction_handler = ReactionHandler()

        list_of_things_to_repeat = [
            lambda: event_handler.wait_and_memorise_an_event(mem),
            lambda: event_handler.personal_events.sleep_wake_up_sleep(),  
            lambda: reaction_handler.general_output(mem),
        ]
        
        self.one_infinite_cicle(list_of_things_to_repeat)


# point 4
class Memory:
    def __init__(self) -> None:
        self._memory = []  # the list of events. Simple liniar model of memory. sdf
        self._event_sentence = ""


class PersonalEvents():
    def sleep_wake_up_sleep(self):
        # every 10 seconds sleep
        sleep_phrase = "I am sleeping..."
        # every 10 seconds awake
        awake_phrase = "I am awake!"
        if round(time.time()%20) < 10:
            print(sleep_phrase)
            return sleep_phrase
        else:
            print(awake_phrase)
            return awake_phrase

    # def die_command(self, )
    

                

# point 3
class EventHandler:

    personal_events = PersonalEvents()

    def handle_the_input_command(self, command: str, *args):
        if command=="die":
            exit()
        if command=="how are you?": # TODO singleton
            print(Mood().mood)


    def unblocking_read(self):
        entered_string = ""

        if msvcrt.kbhit(): 
            key = msvcrt.getch()
            while not key.hex()=="0d":      # press enter to save the phrase
                print(key.decode(), end='', flush=True)  # print each entered key
                entered_string += key.decode()
                key = msvcrt.getch() # wait for new key press
            return entered_string

    # saves input inside memory_instance
    def wait_and_memorise_an_event(self, memory_instance: Memory):
        if msvcrt.kbhit(): 
            key = msvcrt.getch()
            while not key.hex()=="0d":      # press enter to same the phrase
                print(key.decode(), end='', flush=True)  # print each entered key
                memory_instance._event_sentence += key.decode()
                key = msvcrt.getch()
            memory_instance._memory.append(memory_instance._event_sentence)
            self.handle_the_input_command(memory_instance._event_sentence)
            memory_instance._event_sentence = ""

    


        


# point 7
# Reaction
class ReactionHandler():    
    def __init__(self) -> None:
        self.what_to_output = "last_memory"

    def general_output(self, *args, **kwargs):
        if self.what_to_output == "last_memory":
            self.output_last_memory(*args)
        if self.what_to_output == "nothing":
            ...

    def output_last_memory(self, mem: Memory):
        if mem._memory:
                print(mem._memory[-1])


if __name__=="__main__":
    Mood().construct_mood_event_loop_and_boot_it()
