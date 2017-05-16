#=======================================================================
#
#   AUTOMATED FILE TRANSFER PROGRAM
#   AUTHOR: RUSSELL STAUFFER
#   DATE: 16 MAY 2017
#   VERSION: 1.0
#
#   INTERPRETER: PYTHON 2.7.13
#
#   Python Item 64 Exercise
#
#   DESCRIPTION:    This program is designed to transfer text files from
#                   the incoming to outgoing folders if the file was
#                   added or modified 24 hours ago.
#=======================================================================

from datetime import *
import os
import shutil

# Define Variables:
# Source and Destination files

source = "E:/Python/File_Transfer/Incoming/"
origin = os.listdir(source)
destination = "E:/Python/File_Transfer/Outgoing/"

# Time elements
present = datetime.today()
oneDay = timedelta(days = 1)
timecheck = present - oneDay
# print (present,' :Current time')
# print (timecheck,' :Transfer Check Time')

# Process: Checking folders    
for files in origin:
#   print files #file name
    fileTime = os.path.getmtime(source+files) #file timestamp
#   print fileTime
    convFileTime = datetime.fromtimestamp(fileTime) #check date of timestamp
    # Move file if over 1 day old    
    if (convFileTime < timecheck):
        shutil.move(source+files,destination)
        print(files," moved")
        print (convFileTime)
    else:
        print(files," not moved.")
        print (convFileTime)
        
#===== END OF PROGRAM =====
