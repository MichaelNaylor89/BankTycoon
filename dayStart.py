import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Variables as gv
import MyGlobal.Strings as myStrings
import getCustomers as gc
import hireStaff as hs
import statsPage as stats
import helpScreen
import improveBank as ib
import randomEvents as re
import isGameOver as go
import loanManagement as loans
import userSettings

from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3", "4", "9", "u", "h", "s"]

def startDay():
  replit.clear()
  chosenAction = 0
  if gv.dailyActions > 0:
    gm.displayStats()
    print("Main Menu")
    gm.typePrint(myStrings.pleaseChoose)
    print("1. Get more customers.")
    print("2. Hire Staff.")
    print("3. Bank Improvements")
    print("4. Loan Management")
    print("9. Skip to next day")
    print("u. User Settings")

    while chosenAction not in options:
      chosenAction = input(">> ")

    if chosenAction == "1":
      gc.getCustomers()

    if chosenAction == "2":
      hs.newStaff()
    
    if chosenAction == "3":
      ib.improvements()
    
    if chosenAction == "4":
      loans.loanMenu()
    
    if chosenAction == "9":
      replit.clear()
      gm.typePrint("You have " + str(gv.dailyActions) +" actions remaining for the day. Are you sure you want to skip to the next day.[y/n]")

      answer = gm.getAnswer()
      
      if answer == "y":
        advanceDay()
      if answer == "n":
        startDay()

    if chosenAction == "u":
      userSettings.userOptions()

    if chosenAction == "h":
      helpScreen.helpOptions(1)
    
    if chosenAction == "s":
      stats.displayStats()

  else:
    replit.clear()
    gm.typePrint("You have used up all of your actions for the day. Moving to the next day...")
    time.sleep(2)
    advanceDay()


def advanceDay():
  gv.currentDay += 1
  re.eventChance()
  if gv.personalLoans == True:
    loans.tallyLoans()
  gm.typePrint("Tallying staff productivity...")
  staffWork()
  gm.typePrint("Tallying customer deposits...")
  custDeposits()
  gm.typePrint("Tallying customer withdrawals...")
  custWithdrawals()
  gm.typePrint("Adding intrest to accounts...")
  addIntrest()
  gm.typePrint("Paying bills...")
  payBills()
  
  if gv.cash < 0:
    go.bankrupt()
  else:
    gm.typePrint("Refreshing actions...")
    gv.dailyActions = gv.dailyActionAmount
    gm.continuePrompt()
    startDay()
  

def payBills():
  gv.staffCosts = ((gv.marketingStaff * gv.marketingWages) * gv.branches) 
  gv.totalDailyCosts = ((gv.baseCostPerBranch + gv.staffCosts) * gv.branches) + (gv.investorWages * gv.investmentExperts) + (gv.raWages * gv.riskAssessors) + (gv.fixerWages * gv.fixers) + gv.customers
  gv.cash -= gv.totalDailyCosts
  gm.typePrint("Total daily bills $" + str(round((gv.totalDailyCosts))))
  gm.typePrint("Your new balance is $" + str(round(gv.cash)))

def staffWork():
  if gv.totalStaff > 0:
    if gv.marketingStaff > 0:
      marketingProductivity = gv.marketingStaff * gv.branches * gv.bankPopularity
      gv.customers += marketingProductivity
      i = 0
      while i < marketingProductivity:
        gc.addNewCustomer()
        i += 1

      gm.typePrint("Your Marketing Department has signed up " + str(marketingProductivity) + " new customers. Total customers " + str(gv.customers) + ".")
  else:
    gm.typePrint("You have not hired any staff yet.")

def addIntrest():
  dailyIntrest = random.randint(gv.minDailyProfit, gv.maxDailyProfit) / 100

  basicAccTotalIntrest = gv.basicAccountsTotalBalance * dailyIntrest
  savingsAccTotalIntrest = gv.savingsAccountsTotalBalance * dailyIntrest
  premierAccTotalIntrest = gv.premierAccountsTotalBalance * dailyIntrest

  basicAccIntrest = gv.basicAccountsTotalBalance * gv.basicIntrest
  savingsAccIntrest = gv.savingsAccountsTotalBalance * gv.savingsIntrest
  premierAccIntrest = gv.premierAccountsTotalBalance * gv.premierIntrest

  totalDailyIntrest = basicAccTotalIntrest + savingsAccTotalIntrest + premierAccTotalIntrest

  basicEarnings = basicAccTotalIntrest - basicAccIntrest
  savingsEarnings = savingsAccTotalIntrest - savingsAccIntrest
  premierEarnings = premierAccTotalIntrest - premierAccIntrest

  gv.basicAccountsTotalBalance += basicAccIntrest
  gv.savingsAccountsTotalBalance += savingsAccIntrest
  gv.premierAccountsTotalBalance += premierAccIntrest

  gv.cash += basicEarnings + savingsEarnings + premierEarnings

  premierCharges = gv.premierAccounts * 10
  gv.premierAccountsTotalBalance -= premierCharges
  gv.cash += premierCharges

  gm.typePrint("Basic accounts earned $" + str(round(basicAccTotalIntrest)))
  gm.typePrint("Savings accounts earned $" + str(round(savingsAccTotalIntrest)))
  gm.typePrint("Premier accounts earned $" + str(round(premierAccTotalIntrest)))

  gm.typePrint("Basic Account intrest paid to accounts $" + str(round(basicAccIntrest)))
  gm.typePrint("Savings Account intrest paid to accounts $" + str(round(savingsAccIntrest)))
  gm.typePrint("Premier Account intrest paid to accounts $" + str(round(premierAccIntrest)))

  gm.typePrint("You earned $" + str(round(basicEarnings + savingsEarnings + premierEarnings)) + " from investements after intrest has been paid out.")
  gm.typePrint("You earned $" + str(round(premierCharges)) + " from premier account subscription fees")

def custDeposits():
  if gv.customers > 0:
    if gv.basicAccounts > 0:
      basicDepositTotal = 0

      basicDeposits = random.randint(1, gv.basicAccounts)
      depositAmount = random.randint(1, 10) * gv.areaWealthMulti
      
      basicDepositTotal = depositAmount * basicDeposits
      
      gv.basicAccountsTotalBalance += basicDepositTotal
      gm.typePrint("Customers have deposited $" + str(round(basicDepositTotal)) + " into their Basic accounts")
    else:
      gm.typePrint("No basic account deposts")
    
    
    if gv.savingsAccounts > 0:
      savingsDepositTotal = 0

      savingsDeposits = random.randint(1, gv.savingsAccounts)
      depositAmount = random.randint(1, 10) * gv.areaWealthMulti
      savingsDepositTotal = depositAmount * savingsDeposits
      
      gv.savingsAccountsTotalBalance += savingsDepositTotal
      gm.typePrint("Customers have deposited $" + str(round(savingsDepositTotal)) + " into their Savings accounts")
    else:
      gm.typePrint("No savings accounts deposits")

    if gv.premierAccounts > 0:
      premierDepositTotal = 0

      premierDeposits = random.randint(1, gv.premierAccounts)
      depositAmount = random.randint(1, 10) * gv.areaWealthMulti

      premierDepositTotal = depositAmount * premierDeposits
      
      gv.premierAccountsTotalBalance += premierDepositTotal
      gm.typePrint("Customers have deposited $" + str(round(premierDepositTotal)) + " into their Premier accounts")
    else:
      gm.typePrint("No premier account deposts")
  else:
    gm.typePrint("No customer deposits")
  
def custWithdrawals():
  if gv.customers > 0:
    if gv.basicAccounts > 0:
      basicWithdrawalTotal = 0
      basicWithdrawals = random.randint(1, gv.basicAccounts)
      WithdrawalAmount = random.randint(1, 10) * gv.areaWealthMulti
      
      basicWithdrawalTotal = WithdrawalAmount * basicWithdrawals
      
      gv.basicAccountsTotalBalance -= basicWithdrawalTotal
      gm.typePrint("Customers have withdrawn $" + str(round(basicWithdrawalTotal)) + " from their Basic accounts")
    else:
      gm.typePrint("No basic account withdrawals")

    if gv.savingsAccounts > 0:
      savingsWithdrawalTotal = 0

      savingsWithdrawals = random.randint(1, gv.savingsAccounts)
      WithdrawalAmount = random.randint(1, 10) * gv.areaWealthMulti

      savingsWithdrawalTotal = WithdrawalAmount * savingsWithdrawals

      gv.savingsAccountsTotalBalance -= savingsWithdrawalTotal
      gm.typePrint("Customers have withdrawn $" + str(round(savingsWithdrawalTotal)) + " from their Savings accounts")
    else:
      gm.typePrint("No savings account withdrawals")
    
    if gv.premierAccounts > 0:
      premierWithdrawalTotal = 0

      premierWithdrawals = random.randint(1, gv.premierAccounts)
      WithdrawalAmount = random.randint(1, 10) * gv.areaWealthMulti

      premierWithdrawalTotal = WithdrawalAmount * premierWithdrawals
      
      gv.premierAccountsTotalBalance -= premierWithdrawalTotal
      gm.typePrint("Customers have withdrawn $" + str(round(premierWithdrawalTotal)) + " from their Premier accounts")
    else:
      gm.typePrint("No premier account withdrawals")
  else:
    gm.typePrint("No customer withdrawals")
    