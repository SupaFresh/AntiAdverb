import easygui
import sys
from list import alist


def main():

    while 1 == 1:
        reply = easygui.enterbox(msg='Enter a word \n Lowercase only!', title='Anti Adverb', strip=True)
        if reply in alist:
            easygui.msgbox(msg=reply + " is an adverb!", title='Yes', image='images/yes.png')

        elif reply == "":
            print("Error: Nothing Entered")  # restarts loop

        elif reply == "AntiAdverb":
            easygui.msgbox(
                msg="Anti Adverb is a creation of the great SupaFresh! \n "
                    "Find me at https://github.com/SupaFresh \n Happy Writing! \n \n Version 0.7b Alpha \n 10/15/2018",
                title="About Anti Adverb", ok_button="That's Nice")

        elif reply == "killdata":
            sys.exit()

        else:
            easygui.msgbox(msg=reply + " is NOT an adverb!", title='No', image='images/no.png')



if __name__ == '__main__':
    main()
