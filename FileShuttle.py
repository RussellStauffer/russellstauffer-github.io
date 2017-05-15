from shutil import *
import os
# ======================================================================
#   File Shuttle Program
#   Software developer: RUSSELL STAUFFER
#
#   PYTHON VERSION 2.7.13
#
#   Note: This program assumes that you are transferring files from
#   the current directory into a new destination file.
#

# ======================================================================
import shutil
import os
from Tkinter import *

class Application(Frame):
    
    def fileTransfer(self):
        source="E:/Python/File_Shuttle/Folder_A/"
        oldDirectory = os.listdir(source)
#       print oldDirectory
        newDirectory = "E:/Python/File_Shuttle/Folder_B/"

        for files in oldDirectory:
            if files.endswith(".txt"):
                shutil.move(source+files,newDirectory)
                print(files," moved")

    def __init__(self, master):
        Frame.__init__(self,master)
        self.master.minsize (200,30)
        self,master.maxsize (200,30)
        self.master.title("Move Files")
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):
        self.move_Files = Button(self)
        self.move_Files['text'] = "Press to Move Files"
        self.move_Files["command"] = self.fileTransfer
        self.move_Files.pack()
    
    
# === Main Routine starts here ===
root = Tk()
app = Application(root)
app.mainloop()
