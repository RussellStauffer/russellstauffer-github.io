# ===== FOR FILE TRANSFER =====
from tkinter import *
from datetime import *
import os
import shutil
from tkinter import filedialog

def File_Output(source, destination):
#===== FILE TRANSFER FUNCTION =====
# Define Variables:
# Source and Destination files

# source = selectDirectory
	print ("Passed:", source," and ", destination)
	origin = os.listdir(source)
	print ("Origin = ", origin)
# destination = selectObjective

# Time elements
	present = datetime.today()
	print (present)
	oneDay = timedelta(days = 1)
	timecheck = present - oneDay
# print (present,' :Current time')
# print (timecheck,' :Transfer Check Time')

# Process: Checking folders    
	for files in origin:
#   print files #file name
		fileTime = os.path.getmtime(source+'/'+files) #file timestamp
		print (fileTime)
		convFileTime = datetime.fromtimestamp(fileTime) #check date of timestamp
    # Move file if over 1 day old    
		if (convFileTime < timecheck):
			shutil.move(source+'/'+files,destination)
			print(files," moved")
			print (convFileTime)
		else:
			print(files," not moved.")
			print (convFileTime)
			
# Catch if the user clicks on the window upper-right 'X' to ensure they
# want to close.
def ask_quit(self):
	if messagebox.askokcancel("File Transfers complete", "Okay to exit application?"):
		# The app closes
		self.master.destroy()
		os._exit(0)  # Closes all modules, frees memory 
