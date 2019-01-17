import sys
import os
import subprocess
from list import alist
import compileall
import AntiAdverb.maincode
import AntiAdverb.alpabatize_list

try:
    import Tkinter
    from Tkinter import tkMessageBox as dabox  # python 2
except ImportError:
    import tkinter
    from tkinter import messagebox as dabox  # python 3
    
#test if easygui is installed
try:
    import easygui
except ImportError:
    dabox.showerror("Easygui Not Found",
                    "Easygui is not installed on this computer"
                                             )


compileall.compile_dir('AntiAdverb/', force=True)
AntiAdverb.alpabatize_list.main()
AntiAdverb.maincode.main()





