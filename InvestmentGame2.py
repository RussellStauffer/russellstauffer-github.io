#
#	THE INVESTMENT GAME
#       VERSION 2.0
#
#	Programmer:	Russell Stauffer
#	Date: 25 April 2017
#
#       This program will simulate the stock and bond markets, and
#       shows how little an investor can make if they only keep their
#       money in the bank.
#
#       Note: The bonds and stocks are based on real world models
#       and use randomizers to produce different effects every time!
#
#======================================================================	
#
def start(name=""):

	
	name = getName(name)

	print ("Hello, {} welcome to ".format(name))
	print("   The Retirement Game")
	
	avgPortLife = 30       # Average Saving Portfolio = 30 years.
	avgAnnualYield = 1.05  # Yield after 1 average year.
	print("\nIn this game {} you must excel at saving for retirement".format(name)) 
	print (("The average retiree has saved for {} years").format(avgPortLife))
	percAnnualYield = ((avgAnnualYield - 1)*100)
	print ("With an average yield per year of 5%")
	print ("If they save $100 a month during that period, they will have")
	totalSavings = 0
	for x in range (0,avgPortLife):
		totalSavings = (totalSavings + 1200) * avgAnnualYield
	
	totalSavings = round(totalSavings,2)
	print (("saved nearly $  {}").format(totalSavings))
	print (("\n{},Do you think you can do better?").format(name))

	choice = input("Enter y (Yes) or n(No)").lower()
	if (choice == "y"):
		beginGame (name)
	elif (choice == "n"):
		endGame (name)
	else:
		print ("\nI don't understand you choice. Ending program")
	
	
def getName(name):
	print("   The Retirement Game\n")
	name = input("What is your name: ").capitalize()
	return name


def beginGame(name):
	print (("You're a brave person, {}!").format(name))
	
	print("\nWhat kind of investor are you?")
	print("\n1 - Do you like to take risks to get great rewards?")
	print("2 - Are you very cautious with your money?")
	print("3- Do you prefer a little bit of risk for higher rewards?")
	
	investmentType = int (input("\nEnter 1, 2, or 3:   "))
	#return investmentType
		
	if (investmentType == 1):
		print("You would do best with stocks")
		# Do Stock Table with Lists
		stockInvest(name)
	elif (investmentType == 2):
		print("I'd just keep my money in the bank")
		#	Do Bank Investment
		bankInvest(name)
	elif (investmentType == 3):
		print("You should try investment grade bond funds")
		# Do Bonds Table with Tuples
		bondInvest(name)
	else:
		print("You chose nothing. Try again")

		
def stockInvest(name):
	from random import random
	
	print("\nYou can choose from the following stocks:\n")
	print ("\nHere are the stocks you can choose from. Remember that the higher the beta,")
	print (" the higher the risk, or potential rewards\n")
	
	print("\n    Name                  Symbol  Beta  Price")
	stockName = ['U.S.Steel              ',
	             'Tesoro                 ',
                        'Pacific Gas & Electric ',
			'Tesla                  ',
			'Ford Motor             ',]
	stockSymbol = [ 'X   ',
                        'TSO ',
                        'PCG ',
                        'TSLA',
                        'F   ']
	stockBeta = [4.08, 1.21, 0.16, 1.14, 1.36]
	stockPrice = [20.00, 50.00, 30.00, 200.00, 10.00]
	

	for  i in range(0,5):
		print ("  ",(i+1),stockName[i], stockSymbol[i], stockBeta[i]," ", stockPrice[i])

	print("\n")	# spacer
	stockChoice = int(input("Choose a stock using the number beside the name (1-5)"))
	j = stockChoice-1
	print("/nYou have selected ", stockName[j])
	
	# This section is for testing the function. Remove or change for the game.
	k = 0
	yourShares = (1200.0 / stockPrice[j])
	
	while k < 30:
		stockPriceChange = (((random()-0.4)* stockBeta[j])+1)
		stockPrice[j] = stockPrice[j] * stockPriceChange
		if (stockPrice[j] <= 0.0):
			yourShares = 0.0
			stockPrice[j] = (random() * 25) #Bankruptcy protection
			print("Bankruptcy. Company reorganizes. The new stock price is", round(stockPrice[j],2))
		else:
			yourShares = (yourShares + (1200.0 / stockPrice[j]))
		k += 1
	print ("You own ",round(yourShares)," shares of ",stockName[j])
	print ("each share is worth $ ",round(stockPrice[j],2))
	print ("\nYour final worth is: $ ",(round(yourShares * stockPrice[j],2)))
	again(name)
	

def bondInvest(name):
	from random import random
	
	firstBond = ("CALPERS 2040 - 3.5%",1.035,"BBB")
	secondBond = ("City of Portland 2037 - 2%",1.02,"AA+")
	thirdBond = ("State of Illinois 2038 - 5.5%",1.055,"CCC" )
	
	print ("\nSelect one of these three bonds:")
	print ("\nBond Name                              Rating")
	print ("1. ", firstBond[0],"               ",firstBond[2])
	print ("2. ", secondBond[0],"        ",secondBond[2])
	print ("3. ", thirdBond[0],"     ",thirdBond[2])
	
	print("\nRemember that the rating determines the safety. Bonds can go bankrupt!")
	bondChoice = input("Enter your choice (1,2 or 3): ")
		
	if bondChoice == "1":
		print ("\nyou selected: ", firstBond[0]," Not a bad choice")
		defaultRate = .005
		bondRate = firstBond[1]
	elif bondChoice == "2":
		print("\nYou selected:",secondBond[0]," A very safe choice!")
		defaultRate = .001
		bondRate = secondBond[1]
	elif bondChoice == "3":
		print("\nYou chose: ", thirdBond[0]," Risky, a junk bond!")
		defaultRate = .05
		bondRate = thirdBond[1]
	else:
		print ("You forgot to make a choice. Ending program.")
		endGame2()
		
	availableCash = 0.0
	myBonds = 0
	myBondsValue = 0.0
	
	for x in range(1,30):
		availableCash = availableCash + 1200.0
		if myBonds > 0:
			myBondsValue = myBondsValue * bondRate
		if availableCash > 10000:
			myBonds = myBonds + 1
			myBondsValue = (myBondsValue + 10000)
			availableCash = availableCash - 10000
		if defaultRate > random():
			myBonds = 0;
			myBondsValue = 0;
			print("Your bonds defaulted. buying something similar")
	
	finalWorth = round(availableCash + myBondsValue)
	print("In the end, you had ", myBonds, " bonds worth $ ",round(myBondsValue,2))
	print (("and $ {} in cash").format(availableCash))
	print ("for a net worth of $ ",finalWorth)
	again(name)
			

def bankInvest(name):
	print("Bank Routine. This is still under development")
	initialInvestment = 1200.0
	
	for x in range(1,30):
		initialInvestment = initialInvestment * 1.005
		initialInvestment = initialInvestment + 1200
	
	print ("After 30 years of just sticking your money in the bank, you")
	print ("saved a total of $ ", round(initialInvestment,2))
	again(name)
	
def endGame(name):
	print ("What a coward! Ending game.")
	
def endGame2():
	print ("See you later!")

def again(name):
        stop = True
        while stop:
                choice = (input("\nDo you want to try again? (y/n) ").lower())
                if choice == "y":
                        stop = False
                        beginGame(name)
                elif choice == "n":
                        stop = False
                        endGame2()
                else:
                        print("Please enter y for 'yes' or 'n' for no.")
	

#==== The main program starts below.

start()
	

	
	
