# AC - artificial consiousness

import msvcrt
_sum = ""
# main loop
# only inside loop AC can exist
def nastroenie():
    print("I'm born")
    _sum = ""
    while True:
        if msvcrt.kbhit():
            while not msvcrt.getch().hex()=="0d":
                print(msvcrt.getch().hex())
                # _char = msvcrt.getwch()
                # _sum.join(_char)
                input("")
        print(_sum)
        if _sum=="die":
            break


if __name__=="__main__":
    nastroenie()