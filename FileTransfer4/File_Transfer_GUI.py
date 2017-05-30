#======================================================================
"""

	FILE TRANSFER PROGRAM
	GRAPHIC USER INTERFCE (GUI) MODULE
	
	(PYTHON item 66 Exercise)
	
	Version 4.01
	
	30 MAY 2017
	
	Python Ver. 3.6.1
	
	AUTHOR: Russell Stauffer
	
	(SEE File_Transfer.py for full description of this program.)		
"""
#======================================================================
from tkinter import *
from tkinter import filedialog

import File_Transfer
import File_Trans_Func

def layout_GUI(self):
        
		self.btnSource = Button(self.lb1,text='Choose\nSource',command = lambda: File_Trans_Func.getSourceDir(self),fg="blue", width=10, bg="lightgray", bd=2,relief=RAISED, padx=5)
		self.btnSource.grid(row=0,column=0,sticky='w')
		self.btnDest = Button(self.lb1,text='Choose\nSource',command = lambda: File_Trans_Func.getDestinDir(self),fg="blue", width=10, bg="lightgray", bd=2,relief=RAISED, padx=5)
		self.btnDest.grid(row=1,column=0,sticky='w')
	
		self.lblSource = Label(self.lb1,justify=LEFT,fg="green",wraplength=380)
		self.lblSource.grid(row=0,column=1,sticky = 'w')
		self.lblDest = Label(self.lb1,justify=LEFT,fg="red",wraplength=380)
		self.lblDest.grid(row=1,column=1,sticky='w')
	
		self.btnCommit = Button(self.lb1,text='Commit',fg="red", command = lambda: File_Trans_Func.moveFiles(self),width=10, bg="lightgray",bd=2,relief=RAISED, padx=5)
		self.btnCommit.grid(row=2,column=0,sticky='w')
		self.btnClear = Button(self.lb1,text='Clear',fg="blue", command=lambda: File_Trans_Func.clearInfo(self),width=10, bg="lightgray",bd=2,relief=RAISED, padx=5)
		self.btnClear.grid(row=2,column=1,sticky='e')
		self.btnExit = Button(self.lb1,text='Exit',fg="red", command=lambda: File_Trans_Func.ask_quit(self),width=10, bg="lightgray",bd=2,relief=RAISED, padx=5)
		self.btnExit.grid(row=2,column=2,sticky='e')

		self.textInfo = Text(self.lb2, height=4)
		self.textInfo.grid(row=0, column=0)
		self.textInfo.config(state='disabled')
		
		self.scrollCopy = Scrollbar(self.lb3)
		self.textCopy = Text(self.lb3,height=18)
		self.scrollCopy.grid(row=0,column=0)
		self.textCopy.grid(row=0, column=0)
		self.scrollCopy.config(command=self.textCopy.yview)
		self.textCopy.config(yscrollcommand=self.scrollCopy.set)
		self.textCopy.config(state='disabled')
		
		File_Trans_Func.create_TimeTable(self)
		File_Trans_Func.open_TimeTable(self)    
        

if __name__ == "__main__": pass
