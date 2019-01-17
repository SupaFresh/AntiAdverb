import sys
import os
import subprocess
from list import alist
import easygui


def main():
    forfun = os.getcwd()
    while 1 == 1:
        try:
            reply = easygui.enterbox(msg='Enter a word \n Lowercase only!', title='Anti Adverb', strip=True)

            if reply in alist:
                easygui.msgbox(msg=reply + " is an adverb!", title='Yes', image='images/yes.png')

            elif reply == "":
                print("Error: Nothing Entered")  # restarts loop

            elif reply == "AntiAdverb":
                easygui.msgbox(
                    msg="Anti Adverb is a creation of the great SupaFresh! \n "
                        "Find me at https://github.com/SupaFresh \n Happy Writing! \n \n Version 1.0 \n 11/1/2018",
                    title="About Anti Adverb", ok_button="That's Nice")

            elif reply == "killdata":
                sys.exit()  # closes program

            elif reply == "helptips":
                filename = forfun + "/TipsAndTricks.txt"
                f = open(filename, "r")
                text = f.readlines()
                f.close()
                easygui.codebox(filename, "Tips and Tricks", text)

            elif reply == "easygui":
                easygui.abouteasygui()  # Checks easygui version

            else:
                easygui.msgbox(msg=reply + " is NOT an adverb!", title='No', image='images/no.png')

        except Exception:  # Clicking cancel on enterbox exception/freezing
            sys.exit(1)  # solved by closing program silently on exception


if __name__ == '__main__':
    main()
