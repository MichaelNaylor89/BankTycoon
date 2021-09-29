import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Variables as gv
import MyGlobal.Strings as myStrings
import dayStart as ds

from termcolor import cprint as cp
from colorama import *

ynOptions = ["y", "n"]

def bankrupt():
  replit.clear()
  cp("Oh no... You have run out of money", "red")
  gm.typePrint("You have declared bankrupcy, in order to cover your debts and costs you have sold your brances and customer base to a rival bank. After clearing your debts you realise you have just enough to open 1 branch and start again. Would you like to try again? [y/n]")

  answer = ""
  while answer not in ynOptions:
    answer = input(">> ")

  if answer == "y":
    newGame()
  else:
    replit.clear()

def newGame():
  replit.clear()
  ### reset all variables ### also runs at game start as an extra error check
  gv.currentSpeedSetting = "fast"
  gv.typeSpeed = 0.01
  gv.cash = 1000
  gv.currentDay = 1
  gv.branches = 1
  gv.dailyActions = 1
  gv.dailyActionAmount = 1
  gv.bankName = ""
  gv.totalStaff = 0
  gv.marketingStaff = 0
  gv.investmentExperts = 0
  gv.riskAssessors
  gv.marketingWages = 50
  gv.investorWages = 500
  gv.raWages = 2500
  gv.baseCostPerBranch = 150
  gv.marketingStaffCosts = 0
  gv.investmentExpertCosts = 0
  gv.staffCosts = 0
  gv.totalDailyCosts = 0
  gv.extraActionBase = 10000
  gv.newBranchBase = 10000
  gv.localImprovmentsBase = 5000
  gv.popularityBase = 10000
  gv.extraActionMulti = 1
  gv.branchMulti = 1
  gv.customers = 0
  gv.baseNewCustMin = 1
  gv.baseNewCustMax = 10
  gv.areaWealthMulti = 1
  gv.bankPopularity = 1
  gv.basicAccounts = 0
  gv.savingsAccounts = 0
  gv.premierAccounts = 0
  gv.totalAccounts = 0
  gv.basicAccountsTotalBalance = 0
  gv.savingsAccountsTotalBalance = 0
  gv.premierAccountsTotalBalance = 0
  gv.basicIntrest = 0.02
  gv.savingsIntrest = 0.04
  gv.premierIntrest = 0.07
  gv.minDailyProfit = 1
  gv.maxDailyProfit = 10
  gv.loanCapital = 0
  gv.onLoanBalance = 0
  gv.numberOfLoans = 0
  gv.loanRisk = 20
  gv.maxLoans = 5
  gv.loanIntrest = 1.05
  gv.defaultAmount = 0
  gv.defaultMax = 2
  gv.personalLoans = False
  gv.fixers = 0
  fixerWages = 10000
  fixerChance = 0

  gameStart()

def gameStart():
  cp("Congratulations you are ready to open your new bank", "green")
  gm.typePrint("Please choose a name for your bank: ")
  gv.bankName = input(">> ")

  gm.typePrint("Congratulations " + gv.bankName + " is now in business and you have opened your first branch. You need to work hard to keep the bank in business however as you have used almost all of your life savings to get to this point and did not get all if the investments you hoped for. You have $1000 remaining and will be bankrupt in 10 days if you do not take action. Luckily your bank opens today just in time for you to turn things around and make your bank a success.") 

  gm.continuePrompt()

  if gv.bankName == "cheat":
    gv.cash = 1000000
  ds.startDay()
 
newGame()