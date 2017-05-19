"""
        FILE TRANSFER PROGRAM, Version 2.0
        INTERPRETER: PYTHON 3.6.1

        AUTHOR: RUSSELL STAUFFER
        DATE 18-19 MAY 2017

        DESCRIPTION: This program will allow the user to select
        a source folder for text files, and a destination folder.
        All files will be checked for their time of creation or
        last mdofication. If the modification was made less than
        24 hours ago, the file will not be moved. The user must
        then verify that the source and destination are correct
        and hit the "Proceed" button, or they can exit using
        the close button in the upper right corner ("X").

        SUPPORTING MODULES:     File_Transfer_GUI.py
                                File_Transfer_Func.py    

"""
# ===== FOR GENERAL TKINTER GUI OPERATIONS =====
from tkinter import *
import tkinter as tk
# ===== FOR FILE TRANSFER =====
from datetime import *
import os
import shutil
from tkinter import filedialog
from tkinter import messagebox

import File_Transfer_Func
import File_Transfer_GUI

root = Tk()

def main():
# ===== SELECT SOURCE AND DESTINATION =====
	root.directory = filedialog.askdirectory(initialdir = "/")
# print (root.directory)
	selectDirectory = root.directory
	print ("Source directory will be: ", selectDirectory)
	selectObjective = filedialog.askdirectory(initialdir = "/")
	print ("Destination file will be: ",selectObjective)
        #===== Place GUI Here ====
	File_Transfer_GUI.actionButton(selectDirectory, selectObjective)
        
#==== Main Routine =====
	
if __name__ == "__main__":
	main()
