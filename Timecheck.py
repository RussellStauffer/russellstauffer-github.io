import datetime
timePortland = datetime.datetime.now()
timeLondon = datetime.datetime.utcnow()
shiftNewYork = datetime.timedelta(hours = +3)
timeNewYork = timePortland + shiftNewYork

#=== Check Portland ===
print ("In Portland: ", timePortland.strftime('%d %b %I:%M %p'))
portHour = timePortland.strftime('%H')
intPortHour = int(portHour)
if (intPortHour < 9) or (intPortHour > 21):
    print ("Portland Offices are closed.")
else:
    print ("Portland Offices are open!")
#=== Check London ===

londonHour = timeLondon.strftime('%H')
intLondonHour = int(londonHour
                    )
print ("In London: ", timeLondon.strftime('%d %b %I:%M %p'))

if (intLondonHour < 9) or (intLondonHour > 21):
    print ("London Offices are closed.")
else:
    print ("London Offices are open!")

#=== Check New York

newYorkHour = timeNewYork.strftime('%H')
intNewYorkHour = int(newYorkHour)

print ("In New York: ", timeNewYork.strftime('%d %b %I:%M %p'))

if (intNewYorkHour < 9) or (intNewYorkHour > 21):
    print ("New York Offices are closed.")
else:
    print ("New York Offices are open!")


