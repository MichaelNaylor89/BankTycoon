import replit, time, random
import MyGlobal.Methods as gm
import MyGlobal.Strings as myStrings
import MyGlobal.Variables as gv
import statsPage as stats

import helpScreen as hs
import dayStart as ds

from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3", "4", "5", "h", "s"]

billboardCost = 100
paperCost = 3000
radioCost = 40000
tvCost = 500000

billboardMultiplyer = 1
paperMultiplyer = 25
radioMultiplyer = 250
tvMultiplyer = 25000

advertisementCostMulti = 1

def getCustomers():
  replit.clear()

  totalBbCost = gv.branches * (billboardCost * advertisementCostMulti)
  totalPaperCost = gv.branches * (paperCost * advertisementCostMulti)
  totalRadioCost = gv.branches * (radioCost * advertisementCostMulti)
  totalTvCost = gv.branches * (tvCost * advertisementCostMulti)

  chosenAction = 0

  gm.displayStats()
  gm.typePrint("How would you like to get more customers?")
  print(myStrings.pleaseChoose)
  
  ## Options ##
  print(myStrings.backHome)
  print("2. Hire a local billboard for each branch ($ " + str(totalBbCost) + ")")
  print("3. Advertise in the local paper for each branch ($" + str(totalPaperCost) + ")")
  print("4. Advertise on a local radio station for each branch ($" + str(totalRadioCost) + ")")
  print("5. Advertise on a local TV channel for each branch ($" + str(totalTvCost) + ")")

  while chosenAction not in options:
    chosenAction = input(">> ")

  if chosenAction == "1":
    ds.startDay()

  ### Billboard Action ###
  if chosenAction == "2":
    gm.typePrint("This will use up 1 action and will cost you $" + str(billboardCost) + " per branch that you own. \n Total current cost = $" + str(totalBbCost))
    gm.typePrint("Do you wish to continue with this purchase? [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      if gv.cash >= totalBbCost:
        advertise(totalBbCost, billboardMultiplyer)
      else:
        cantAfford(totalBbCost)
    else:
      cancelPurchase()

  ### paper action ###
  if chosenAction == "3":
    gm.typePrint("This will use up 1 action and will cost you $" + str(paperCost) + " per branch that you own. \n Total current cost = $" + str(totalPaperCost))
    gm.typePrint("Do you wish to continue with this purchase? [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      if gv.cash >= totalPaperCost:
        advertise(totalPaperCost, paperMultiplyer)
      else:
        cantAfford(totalPaperCost)
    else:
      cancelPurchase()
   
  ### Radio Action ###
  if chosenAction == "4":
    gm.typePrint("This will use up 1 action and will cost you $" + str(radioCost) + " per branch that you own. \n Total current cost = $" + str(totalRadioCost))
    gm.typePrint("Do you wish to continue with this purchase? [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      if gv.cash >= totalRadioCost:
        advertise(totalRadioCost, radioMultiplyer)
      else:
        cantAfford(totalRadioCost)
    else:
      cancelPurchase()

  ### TV Action ###
  if chosenAction == "5":
    gm.typePrint("This will use up 1 action and will cost you $" + str(tvCost) + " per branch that you own. \n Total current cost = $" + str(totalTvCost))
    gm.typePrint("Do you wish to continue with this purchase? [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      if gv.cash >= totalTvCost:
        advertise(totalTvCost, tvMultiplyer)
      else:
        cantAfford(totalTvCost)
    else:
      cancelPurchase()

  ### Help action ###
  if chosenAction == "h":
    hs.helpOptions(3)

  if chosenAction == "s":
    stats.displayStats()

### Advertise Method ###

def advertise(cost, multiplyer):
  replit.clear()
  gv.cash -= cost
  newCustAmount = gm.customerAmount(multiplyer)
  gm.typePrint("Congratulations " + str(gv.bankName) + " has " + str(newCustAmount) + " new customer(s). Returning to home screen...")
  i = 0
  while i < newCustAmount:
    addNewCustomer()
    i += 1
  gv.customers += newCustAmount
  time.sleep(2)
  gv.dailyActions -= 1
  ds.startDay()

### New customer Method###

def addNewCustomer():
  numAccounts = random.randint(1, 3)

  if numAccounts == 1:
    gv.basicAccounts += 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts

    gv.basicAccountsTotalBalance += gm.accountAmount(numAccounts)

  if numAccounts == 2:
    gv.basicAccounts += 1
    gv.savingsAccounts += 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts

    gv.basicAccountsTotalBalance += gm.accountAmount(numAccounts)
    gv.savingsAccountsTotalBalance += gm.accountAmount(numAccounts)


  if numAccounts == 3:
    gv.savingsAccounts += 1
    gv.premierAccounts += 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts
    
    gv.savingsAccountsTotalBalance += gm.accountAmount(numAccounts)
    gv.premierAccountsTotalBalance += gm.accountAmount(numAccounts)
    
def cancelPurchase():
  replit.clear()
  gm.typePrint("Purchase cancelled returning you to the Get Customers screen...")
  time.sleep(1.5)
  getCustomers()

def cantAfford(cost):
  replit.clear()
  gm.typePrint("You cannot afford this right now. You are $" + str(cost - gv.cash) + " short. Returning you to the get Customers screen...")
  time.sleep(1.5)
  getCustomers()