import  replit, time, random
import MyGlobal.Methods as gm
import MyGlobal.Strings as myStrings
import MyGlobal.Variables as gv
import statsPage as stats
import helpScreen as hs
import dayStart as ds


from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3", "4", "5", "6" "h", "s"]

def loanMenu():
  replit.clear()

  if gv.personalLoans == True:
    cp("Welcome to the Loan Management Screen", "green")

    chosenAction = 0
    gm.displayStats()
    gm.typePrint(myStrings.pleaseChoose)

    reduceRiskCost = 10000 * (21 - gv.loanRisk)
    increaseMaxCost = 10000 * gv.maxLoans
    reduceDefaultChanceCost = gv.defaultMax * (5000 + (gv.numberOfLoans * 10))

    print(myStrings.backHome)
    print("2. Add to loan fund")
    print("3. Remove from loan fund")
    print("4. Reduce risk ($" + str(reduceRiskCost) + ")")
    print("5. Increase Max Loans ($" + str(increaseMaxCost) + ")")
    print("6. Reduce default chance ($" + str(reduceDefaultChanceCost) + ")")

    while chosenAction not in options:
      chosenAction = input(">> ")

    if chosenAction == "1":
      ds.startDay()
    
    if chosenAction == "2":
      addFunds()

    if chosenAction == "3":
      removeFunds()

    if chosenAction == "4":
      reduceRisk(reduceRiskCost)

    if chosenAction == "5":
      increaseMax(increaseMaxCost)
    
    if chosenAction == "6":
      reduceDefaultChance(reduceDefaultChanceCost)
    
    if chosenAction == "h":
      hs.helpOptions(5)
    
    if chosenAction == "s":
      stats.displayStats()

  else:
    gm.typePrint("Your bank is not yet equipped to handle personal loans. When you have enough cash you open up this option from the Bank Improvments Page. Returning you to the home screen...")
    time.sleep(1.5)
    ds.startDay()

def addFunds():
  replit.clear()
  gm.typePrint("You can add cash to your loan fund so that the bank has more money available to lend. Due to regulatory restrictions deposits are limited to 10% of your available cash. Please enter a number beween 1 and 10 below or enter b to go back or h to go home.")

  possValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "b", "h"]
  value = ""
  while value not in possValues:
    value = input(">> ")
  
    if value == "b":
      replit.clear()
      gm.typePrint("going back...")
      time.sleep(0.5)
      loanMenu()

  if value == "h":
    replit.clear()
    gm.typePrint("Returning home...")
    time.sleep(1)
    ds.startDay()

  else:
    replit.clear()
    cost = round(round(gv.cash / 100) * int(value))
    gm.typePrint("You have chosen to add " + str(value) + "% of your current cash which is $" + str(cost) + " to the loan fund. Do you wish to continue? [y/n]")

    answer = gm.getAnswer()

    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.loanCapital += cost
      gm.typePrint("$" + str(cost) + " has been added to the load fund. Returning home...")
      time.sleep(1.5)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()

def removeFunds():
  replit.clear()
  if gv.loanCapital > (100000):
    gm.typePrint("You can withdraw 10% of your loanCapital to your current funds per action used. Would you like to do this now [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      amount = gv.loanCapital / 10
      gv.cash += amount
      gv.loanCapital -= amount
      gm.typePrint("You have withdrawn $" + str(amount) + " to your current funds. Returning to home screen...")
      time.sleep(1)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()
  else:
    gm.typePrint("You have under 100000 Loan Capital available and cannot withdraw right now. Returning to Loan Management screen...")
    time.sleep(1)
    loanMenu()

def increaseMax(cost):
  replit.clear
  if gv.cash > cost:
    gm.typePrint("By bringing in more support staff you are able to approve more loans each day. This will cost $" + str(cost) + " and will use up one action. Do you wish to continue [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      gv.cash -= cost
      gv.maxLoans += 1
      gm.typePrint("You have increased your max loans per day. Your new max is " + str(gv.maxLoans) + ". Returning to home screen...")
      time.sleep(1)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()
  else:
    tooExpensive(cost)

def reduceRisk(cost):
  replit.clear()
  if gv.loanRisk > 10:
    if gv.cash > cost:
      gm.typePrint("By hiring more staff to select loan applicants more carefully and attract more reliable borrowers you are able to reduce risk. This means you will usually make more from loan repayments. This will cost $" + str(cost) + " and will use up one action. Do you wish to continue [y/n]")
      answer = gm.getAnswer()

      if answer == "y":
        gv.cash -= cost
        gv.loanRisk -= 1
        gm.typePrint("You have reduced your loan risk, your current loan replayment risk is " + str(gv.loanRisk) + "%. Returning you to the home screen...")
        time.sleep(1)
        gv.dailyActions -= 1
        ds.startDay()
      else:
        cancelPurchase()
    else:
      tooExpensive(cost)

  else:
    gm.typePrint("You have already reduced the risk as much as you can. Returning to Loan Management screen...")
    time.sleep(1)
    loanMenu()    

def reduceDefaultChance(cost):
  replit.clear()
  if gv.cash > cost:
    gm.typePrint("Customers that miss payments have a chance to default causing all the money they owe you to be written off as a loss. Increase the size of your in house collections team to try prevent customers defaulting on their loans when not paying. The current chance of default is 1 in " + str(gv.defaultMax) + " for customers that miss payments. This will cost $" + str(cost) + " and will use up one action. Do you wish to continue? [y/n]")
    answer = gm.getAnswer()

    if answer == "y":
      gv.cash -= cost
      gv.defaultMax += 1
      gm.typePrint("You have reduced the chance for customers who miss payments to default. The new chance is 1 in " + str(gv.defaultMax) + ". Returning you to the home screen...")
      time.sleep(1)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()

  else:
    tooExpensive(cost)

def cancelPurchase():
  replit.clear()
  gm.typePrint("Deposit cancelled returning you to the loan management screen screen...")
  time.sleep(1.5)
  loanMenu()

def tooExpensive(cost):
  gm.typePrint("You are currently unable to afford this upgrade. You are $" + str(cost - gv.cash) + " short. Returning to Loan Management screen...")
  time.sleep(1)
  loanMenu()

def tallyLoans():
  if gv.onLoanBalance > 0:
    gv.onLoanBalance *= gv.loanIntrest

    i = 0
    while i < gv.numberOfLoans:
      loanPerformance()
      i += 1

  giveLoans()

def giveLoans():
  numLoans = (gv.branches * random.randint(1, gv.maxLoans))

  i = 0
  while i < numLoans:
    giveLoan()
    i += 1

def giveLoan():
  loanAmount = random.randint(1, round(gv.loanCapital / (gv.branches * gv.maxLoans)))

  if loanAmount < gv.loanCapital:
    gv.numberOfLoans += 1
    gv.loanCapital -= loanAmount
    gv.onLoanBalance += loanAmount

def loanPerformance():
  chance = random.randint(1,100)
  amount = (gv.onLoanBalance / gv.numberOfLoans) /10
  if chance > gv.loanRisk:
    gv.loanCapital += amount
    gv.onLoanBalance -= amount
  else:
    defaultChance = random.randint(1,gv.defaultMax)
    if defaultChance == 1:
      gv.numberOfLoans -= 1
      gv.onLoanBalance -= amount
      gv.defaultAmount += amount