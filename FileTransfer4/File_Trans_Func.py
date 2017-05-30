#======================================================================
"""

	FILE TRANSFER PROGRAM
	FUNCTIONS MODULE

	
	(PYTHON item 66 Exercise)
	
	Version 4.01
	
	30 MAY 2017
	
	Python Ver. 3.6.1
	
	AUTHOR: Russell Stauffer
	
	(SEE File_Transfer.py for full description of this program.)		
"""
#======================================================================
import datetime
import time
import sqlite3
import shutil
from tkinter import *
from tkinter import filedialog
import os

def getSourceDir(self):
    directory = filedialog.askdirectory(initialdir = "/", title = "Select Your Source Directory")
    self.lblSource.config(text=directory+'/')
    self.btnSource.config(state="disabled")
	
def getDestinDir(self):
    directory = filedialog.askdirectory(initialdir = "/", title = "Select Your Destination Directory")
    self.lblDest.config(text=directory+'/')
    self.btnDest.config(state="disabled")

def moveFiles(self):
    # Get folder destinations
    # print(self.lblSource, ", type is:", type(self.lblSource))
	source = self.lblSource.cget('text')
	destination = self.lblDest.cget('text')
	# if source != '' and destination != '':
	
	#--- Get current time ---
	rightNow = datetime.datetime.now()
	
	#--- Get Last Access time ---
	conn = sqlite3.connect('LastCopy.db')
	c = conn.cursor()
    #--- Find the most recent access (largst rowid) ---
	c.execute("SELECT time FROM tblLastTime WHERE rowid = (SELECT MAX(rowid) FROM tblLastTime)")
	lastAccessTime = c.fetchone()
	# print ("Last Access time (moveFiles) :", lastAccessTime)
	lastAccess = lastAccessTime[0]
	print ("Last Access was : ",lastAccess)
	#--- Get list  of files in the source directory ---
	incomingList = os.listdir(source)
	self.textCopy.config(state='normal')
	self.textCopy.delete(1.0, END)
	#--- Check file last modification time
	j = 0
	k = 0
	for i in incomingList:
		fileTime = os.path.getmtime(source+i)
        # ---new solution. Move if older than last access
		print (fileTime)
		j = j+1
		if (fileTime > lastAccess):
			# Move files if older than today.
			# if rightNow.year == fileTime.tm_year and rightNow.month == fileTime.tm_mon and rightNow.day == fileTime.tm_mday:
			#--- Old solution. Use new solution below ---
			shutil.move(source+i, destination+i)
			self.textCopy.insert(END, i+'\n')
			k = k+1
    # --- Add time stamp to the file --- 
	addTimeStamp(self)
	# print (j,"files checked, ",k," files moved" )
	self.textInfo.config(state='normal')
	self.textInfo.delete(1.0, END)
	self.textInfo.insert(END, str(j)+" files accessed: "+ str(k) +", files moved\n")
	self.textInfo.config(state='disabled')
	
	self.textCopy.config(state='disabled')
    
    
def clearInfo(self):
    self.btnSource.config(state='normal')
    self.btnDest.config(state='normal')

    self.textInfo.config(state='normal')
    # self.textInfo.delete(1.0, END)
    self.textInfo.insert(END, 'TIMESTAMP HAS BEEN UPDATED:\n')
    self.textInfo.config(state='disabled')

    self.textCopy.config(state='normal')
    self.textCopy.delete(1.0, END)
    self.textCopy.insert(END, '')
    self.textCopy.config(state='disabled')

    self.lblSource.config(text='')
    self.lblDest.config(text='')


def ask_quit(self):
	if messagebox.askokcancel("Exit program", "Okay to exit application?"):
		# The app closes
		self.master.destroy()
		os._exit(0)  # Closes all modules, frees memory 
#
def open_TimeTable(self):
	conn = sqlite3.connect('LastCopy.db')
	c = conn.cursor()
    #--- Find the most recent access (largst rowid) ---
	c.execute("SELECT date FROM tblLastTime WHERE rowid = (SELECT MAX(rowid) FROM tblLastTime)")
	lastAccessTime = c.fetchone()
	lastChkDate = lastAccessTime[0]
	# print ("Last Access time (open_Table) :", lastAccessTime)
	self.textInfo.config(state='normal')
	self.textInfo.insert(END, 'Files were last checked at: '+lastChkDate+'\n')
	self.textInfo.config(state='disabled')  
    # print("lastAccessTime = ", lastAccessTime)
    #--- Converting tuple in lastTime
	lastAccess = lastAccessTime
	# print ("LastAccess (float) = ",self.lastAccess)
	return(lastAccess)

def create_TimeTable(self):
	conn = sqlite3.connect('LastCopy.db')
	c = conn.cursor()
	c.execute("SELECT COUNT(*) FROM tblLastTime") 
	count = c.fetchone()[0]
	if count < 1:
		c.execute("CREATE TABLE IF NOT EXISTS tblLastTime(date string, time real);")
		conn.commit()
		addTimeStamp(self)
		print("NEW TIMESTAMP GENERATED:(Create_TimeTable)")
	conn.close()

    

def addTimeStamp(self):
	currTime = time.time()
	currDate = time.asctime()
#	print ("CurrTime is:", currTime)
#	print ("type (currTime)is ",type(currTime))
	# currDate = time.strftime("%d/%m/%Y")
	conn = sqlite3.connect('LastCopy.db')
	with conn:
		c = conn.cursor()
		# c.execute("INSERT INTO tblLastTime (date,time) VALUES (?,?)",(currDate,currTime))
		c.execute("INSERT INTO tblLastTime(date, time) VALUES (?,?)",(currDate, currTime))
		conn.commit()
	conn.close()
