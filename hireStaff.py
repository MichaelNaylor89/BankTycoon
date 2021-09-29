import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Variables as gv
import MyGlobal.Strings as myStrings
import getCustomers as gc
import dayStart as ds

import helpScreen
import statsPage as stats
from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3", "4", "5", "h", "s"]

staffBaseCost = 1000
marketingMultiplyer = 1
investmentExpertMultiplyer = 20
riskAssessorMultiplyer = 50
fixerMultiplyer = 1000

def newStaff():
  meCost = gv.branches * staffBaseCost * marketingMultiplyer
  ieCost = staffBaseCost * investmentExpertMultiplyer
  raCost = staffBaseCost * riskAssessorMultiplyer
  fixerCost = staffBaseCost * fixerMultiplyer
  chosenAction = 0
  replit.clear()
  gm.displayStats()
  gm.typePrint("Hire some staff to automate actions each day. Hiring new staff increase your daily costs in addition to the initial cost to recruit them.")
  gm.typePrint(myStrings.pleaseChoose)
  
  print(myStrings.backHome)
  print("2. Hire a Marketing Expert ($" + str(meCost) + ")")
  print("3. Hire an investment Expert ($" + str(ieCost) + ")")
  print("4. Hire a risk assessor ($" + str(raCost) + ")")
  print("5. Hire a fixer ($ " + str(fixerCost) + ")")

  while chosenAction not in options:
    chosenAction = input(">> ")

  if chosenAction == "1":
    ds.startDay()

  if chosenAction == "2":
    if gv.cash > meCost:
      hireMarketing(meCost)
    else:
      replit.clear()
      gm.typePrint("You cannot afford a new marketing expert you are $" + str(meCost - gv.cash) + " short. Returning to the hiring screen...")
      time.sleep(1.5)
      newStaff()
  
  if chosenAction == "3":
    if gv.cash > ieCost:
      hireInvestor(ieCost)
    else:
      replit.clear()
      gm.typePrint("You cannot afford to hire an Investment Expert right now. You are $" + str(ieCost - gv.cash) + " short. Returning you to the hiring screen...")
      time.sleep(1.5)
      newStaff()

  if chosenAction == "4":
    if gv.cash > raCost:
      hireRiskAssessor(raCost)
    else:
      replit.clear()
      gm.typePrint("You cannot afford to hire a Risk Assessor right now. You are $" + str(raCost - gv.cash) + " short. Returning you to the hiring screen...")
      time.sleep(1.5)
      newStaff()
  
  if chosenAction == "5":
    if gv.cash > fixerCost:
      hireFixer(fixerCost)
    else:
      replit.clear()
      gm.typePrint("You cannot afford to hire a Fixer right now. You are $" + str(fixerCost - gv.cash) + " short. Returning you to the hiring screen...")
      time.sleep(1.5)
      newStaff()
  
  if chosenAction == "h":
    helpScreen.helpOptions(2)

  if chosenAction == "s":
    stats.displayStats()

def hireMarketing(cost):
  replit.clear()
  costIncrease = 0
  costIncrease = gv.branches * gv.marketingWages
  gm.typePrint("A Marketing Expert will use their skills to bring in new customers. Each Marketing Expert will being in 1 new customer per day.")
  gm.typePrint("To hire a new Markering Expert for every branch you will need to pay $" + str(cost) + " and your daily costs will be increased by $" + str(costIncrease) + " per day. You will also use up 1 action. \n Would you like to continue with this recruitment? [y/n]")

  answer = gm.getAnswer()
    
  if answer == "y":
    replit.clear()
    gv.cash -= cost
    gv.marketingStaff += 1
    gv.totalStaff += 1
    replit.clear()
    gm.typePrint("Congratulations you have hired a new Marketing Expert in each of your branches. Returning to the home screen...")
    time.sleep(1)
    gv.dailyActions -= 1
    ds.startDay()
  else:
    replit.clear()
    gm.typePrint("Recruitment cancelled returning to staff hire screen...")
    time.sleep(1)
    newStaff()
 
def hireInvestor(cost):
  replit.clear()
  gm.typePrint("Hiring an Investment Expert will help you to earn more from investments each day. Each Investment Expert will increase your max daily earnings from investing by 0.01%. Your current max is " + str(gv.maxDailyProfit/100) + "%")
  gm.typePrint("A new Investment Expert will cost you $" + str(cost) + " and increase your daily costs by $" + str(gv.investorWages) + " would you like to continue with this recruitment? [y/n]")

  answer = gm.getAnswer()

  if answer == "y":  
    gv.cash -= cost
    gv.investmentExperts += 1
    gv.totalStaff += 1
    gv.maxDailyProfit += 1
    investmentExpertMultiplyer * 1.5
    gm.typePrint("Congratulations you have hired a new Investment Expert. Returning to the home screen...")
    time.sleep(1)
    gv.dailyActions -= 1
    ds.startDay()
  else:
    replit.clear()
    gm.typePrint("Recruitment cancelled returning to staff hire screen...")
    time.sleep(1)
    newStaff()

def hireRiskAssessor(cost):
  replit.clear()
  gm.typePrint("Hiring a Risk Assessor will help you to earn more from investments each day. Each Risk Assessor will increase your minimum daily earnings from investing by 0.01%. Your current min is " + str(gv.minDailyProfit/100) + "%")
  gm.typePrint("A new Investment Expert will cost you $" + str(cost) + " and increase your daily costs by $" + str(gv.raWages) + " would you like to continue with this recruitment? [y/n]")

  answer = gm.getAnswer()

  if answer == "y":  
    gv.cash -= cost
    gv.riskAssessors += 1
    gv.totalStaff += 1
    gv.minDailyProfit += 1
    riskAssessorMultiplyer * 2
    gm.typePrint("Congratulations you have hired a new Risk Assessor. Returning to the home screen...")
    time.sleep(1)
    gv.dailyActions -= 1
    ds.startDay()
  else:
    replit.clear()
    gm.typePrint("Recruitment cancelled returning to staff hire screen...")
    time.sleep(1)
    newStaff()

def hireFixer(cost):
  replit.clear()
  gm.typePrint("No one can stop random events occuring they are a fact of life. Fixers however can sometimes make sure that events move in your favour when they do. Every fixer gives a 1% chance of turning a negative random event into a positive one. A new fixer will cost $" + str(cost) + " and increase your daily costs by " + str(gv.fixerWages) + ". Do you wish to continue with this recruitment? [y/n]")

  answer = gm.getAnswer()

  if answer == "y":  
    gv.cash -= cost
    gv.fixers += 1
    gv.totalStaff += 1
    gv.fixerChance += 1
    fixerMultiplyer * 2.5
    gm.typePrint("Congratulations you have hired a new Fixer. Returning to the home screen...")
    time.sleep(1)
    gv.dailyActions -= 1
    ds.startDay()
  else:
    replit.clear()
    gm.typePrint("Recruitment cancelled returning to staff hire screen...")
    time.sleep(1)
    newStaff()

  