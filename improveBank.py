import  replit, time, random
import MyGlobal.Methods as gm
import MyGlobal.Strings as myStrings
import MyGlobal.Variables as gv
import statsPage as stats
import hireStaff as staff

import helpScreen as hs
import dayStart as ds

from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3", "4", "5", "6", "h", "s"]

def improvements():
  replit.clear()
  chosenAction = 0

  extraActionCost = gv.extraActionBase * gv.extraActionMulti
  branchCost = (gv.newBranchBase * gv.branchMulti) + ((staff.staffBaseCost * staff.marketingMultiplyer) * gv.marketingStaff )
  improveCost = (gv.areaWealthMulti * gv.branches) * 5000
  improveImageCost = (gv.bankPopularity * 25000) 
  
  plCost = 100000

  gm.displayStats()
  gm.typePrint("Welcome to the bank inprovements area. Here you can buy expensive but powerful upgrades to your bank. What would you like to improve?")
  print(myStrings.pleaseChoose)

  ## Options ##
  print(myStrings.backHome)
  print("2. Open new Branch ($" + str(branchCost) + ")")
  print("3. More actions per day ($" + str(extraActionCost) + ")")
  print("4. Improve Local Area ($" + str(improveCost) + ")")
  print("5. Improve your Popularity ($" + str(improveImageCost) + ")")
  
  if gv.personalLoans == False:
    print("6. Offer personal Loans ($" + str(plCost) + ")")
  else:
    print("6. Offer personal Loans (Already Unlocked)")

  while chosenAction not in options:
    chosenAction = input(">> ")

  if chosenAction == "1":
    ds.startDay()
  
  if chosenAction == "2":
    newBranch(branchCost)

  if chosenAction == "3":
    moreActions(extraActionCost)

  if chosenAction == "4":
    improveLocalArea(improveCost)
  
  if chosenAction == "5":
    improvePopularity(improveImageCost)
  
  if chosenAction == "6":
    unlockLoans(plCost)

  ### Help action ###
  if chosenAction == "h":
    hs.helpOptions(4)

  if chosenAction == "s":
    stats.displayStats()

def newBranch(cost):
  replit.clear()
  if gv.cash > cost:
    gm.typePrint("Opening a new branch will cost $" + str(cost) + ". You will also use up 1 action and your daily costs will be inceased to cover the cost of staff and bills for the new branch. Opening a new branch will improve your business effectiveness in many areas. Do you wish to continue this purchase? [y/n]")
    answer = gm.getAnswer()
    
    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.branches += 1
      gv.branchMulti *= 1.15
      gm.typePrint("You have successfully opened a new branch. You now have " + str(gv.branches) + " branches. Returning to the main menu...")
      time.sleep(1.5)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()    
  else:
    cantAfford(cost)

def moreActions(cost):
  replit.clear()
  if gv.cash > cost:
    gm.typePrint("Buying 1 more action per day will cost $" + str(cost) + ". No actions will be removed for this purchase but your new increased action amount will not take effect until tomorrow. Are you sure you wish to make this purchase?[y/n]")
    answer = gm.getAnswer()
    
    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.dailyActionAmount += 1
      gv.extraActionMulti *= 2
      gm.typePrint("Purchase complete. You will now have 1 extra action per day giving you " + str(gv.dailyActionAmount) + " actions each day. Returning you to the home screen...")
      time.sleep(1.5)
      ds.startDay()
    else:
      cancelPurchase()
  else:
    cantAfford(cost)

def improveLocalArea(cost):
  replit.clear()
  if gv.cash > cost:
    gm.typePrint("Improving the local area get more expensive each time you do it and with each branch you buy. Investing in your local area however has far reaching effects and will improve the wealth of everyone around you. Why do you care? Well improving local wealth improves customer wealth. This means new customers open accounts with more money and deposit more money. They also have more places to spend their cash so they will withdraw more money too so this action is not without risk. \n " + "Do you wish to continue? [y/n]")

    answer = gm.getAnswer()

    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.areaWealthMulti += 1
      gm.typePrint("You have invested in the local area improving the lives and wealth of everyone near your brances. This will increase every transaction your customers make with you. Returning to main menu...")
      time.sleep(1.5)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()
  else:
    cantAfford(cost)

def improvePopularity(cost):
  replit.clear()
  if gv.cash > cost:
    
    gm.typePrint("Improving the popularity of your bank makes your advertising campigns to get customers more effective and make your Marketing Experts more effective in their daily recruitment. Would you like to continue with this purchase? [y/n]")

    answer = gm.getAnswer()

    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.bankPopularity += 1
      gm.typePrint("You have contacted various social media influencers and celebriteies and paid them to endorse your bank. Overall public perception of you has improved and customers are now more likely to join your bank")
      time.sleep(1.5)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()
  else:
    cantAfford(cost)

def unlockLoans(cost):
  replit.clear()
  if gv.personalLoans == True:
    gm.typePrint("You have already unlocked this feature. Taking you back to the improvements screen...")
    time.sleep(1.5)
    improvements()
  
  if gv.cash > cost:
    gm.typePrint("Offering personal loans is a high risk venture with high profit margins when successful. Because of the risk involved a seperate pot of cash will be used for loans. To start offering personal loans you will need to pay $" + str(cost) + ", half of this will be used to advertise the new service and set up the systems required for your staff and half will be used as starting capital for the loan fund. You will also use up 1 action. \n" )
    gm.typePrint("Do you wish to continue? [y/n]")

    answer = gm.getAnswer()

    if answer == "y":
      replit.clear()
      gv.cash -= cost
      gv.loanCapital += (cost/2)
      gv.personalLoans = True
      gm.typePrint("Excellent your bank now offers personal loans. You can now access the loan management screen from the home screen. Returning you to the home screen...")
      time.sleep(1.5)
      gv.dailyActions -= 1
      ds.startDay()
    else:
      cancelPurchase()
  else:
    cantAfford(cost)

def cancelPurchase():
  replit.clear()
  gm.typePrint("Purchase cancelled returning you to the improvments screen...")
  time.sleep(1.5)
  improvements()

def cantAfford(cost):
  replit.clear()
  gm.typePrint("You cannot afford this right now. You are $" + str(cost - gv.cash) + " short. Returning you to the bank improvements screen...")
  time.sleep(1.5)
  improvements()
  

  