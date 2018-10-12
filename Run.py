import easygui
from list import alist

while 1 == 1:
    reply = easygui.enterbox(msg = 'Enter a word \n Lowercase only!', title = 'Anti Adverb', strip = True)
    if reply in alist:
        easygui.msgbox(reply + " is an adverb!")
        
    elif reply == "":
        print("Retry that")
        easygui.exceptionbox()
        
    elif reply == "AntiAdverb":
        easygui.msgbox(msg = "Anti Adverb is a creation of the great SupaFresh! \n Find me at https://github.com/SupaFresh \n Happy Writing! \n \n Version 0.5b Alpha \n 10/12/2018", title = "About Anti Adverb", ok_button = "That's Nice")
    
    else:
        easygui.msgbox(reply + " is NOT an adverb!")
        
print("Uh Oh!")
    