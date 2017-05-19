from tkinter import *
import tkinter as tk

import File_Transfer_Func
# import File_Transfer

def actionButton(inputSelect, outputSelect):
	print ("Button inputs: ", inputSelect," and ", outputSelect)
	
	tk.Label(text ="You will transfer files from: ").grid(row=0, column = 0 )
	tk.Label(text = inputSelect).grid(row = 1, column = 0)
	tk.Label(text = "And send them to: ").grid(row= 2, column = 0)
	tk.Label(text = outputSelect).grid(row = 3, column=0)

	tk.Button(text = "Proceed", width = 12, height =2, command = lambda: File_Transfer_Func.File_Output(inputSelect, outputSelect)).grid(row=4,column=0)
