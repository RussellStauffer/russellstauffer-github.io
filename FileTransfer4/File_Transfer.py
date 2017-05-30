"""
	FILE TRANSFER PROGRAM
	
	(PYTHON item 66 Exercise)
	
	Version 4.01
	
	30 MAY 2017
	
	Python Ver. 3.6.1
	
	AUTHOR: Russell Stauffer
	
	DESCRIPTION: This program lets a user select file locations to 
	transfer between, based on the last time this program was accessed.
	The idea behind this program is that a user may need to transfer 
	files to another location on a network, based on a periodic need
	to initiate when a user is ready and able to transfer. Previous
	versions of this program did so automatically every 24 hours, but
	if files were even a few seconds late in betting turned into the
	source file, the files would miss the transfer and be late. Manual
	execution was considered a better option, allowing for delay when
	necessary.

"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import File_Transfer_GUI
import File_Trans_Func

class FileCopy(Frame):
    def __init__(self, master):
        
        self.master = master
        master.title("File Relocator")
        
        master.resizable(False,False)
        master.geometry('540x380+0+0')

        self.master.protocol("WM_DELETE_WINDOW", lambda: File_Trans_Func.ask_quit(self))
    	
        self.frameBase=Frame(self.master, bd = 5, bg = "red")
        self.frameBase.pack(expand=1, fill=tk.BOTH)
        
        self.lb1 = LabelFrame(self.frameBase, text = "Copy new or modified files", relief=RIDGE)
        self.lb1.pack(fill=tk.BOTH)

        self.lb2 = LabelFrame(self.frameBase, text = "Information", relief=RIDGE)
        self.lb2.pack()
                      
        self.lb3 = LabelFrame(self.frameBase, text = "Files Transferred:", relief = RIDGE)
        self.lb3.pack(fill = tk.BOTH, expand=1)

        File_Transfer_GUI.layout_GUI(self)

#===== MAIN ROUTINE STARTS HERE ==========
def main():
    root = Tk()	
    app = FileCopy(root)
    root.mainloop()
if __name__ == "__main__":	main()
