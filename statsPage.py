import time, replit
from termcolor import cprint as cp
from colorama import *

import MyGlobal.Variables as gv
import MyGlobal.Methods as gm
import dayStart as ds

def displayStats():
  replit.clear()

  gm.typePrint("Fetching stats....")
  time.sleep(1)
  cp("***STATS***", "green")
  print("Current Day: " + str(gv.currentDay))
  print("Current cash: " + str(gv.cash))
  print("Max Daily Actions: " + str(gv.dailyActionAmount))
  print("Number of Branches: " + str(gv.branches) + "\n")
  

  
  cp("***CUSTOMER STATS***", "green")
  print("Total customers: " + str(round(gv.customers)))
  print("Total Accounts: " + str(gv.totalAccounts))
  
  print("Basic Accounts: " + str(gv.basicAccounts))
  print("Basic Accounts Balance: $" + str(round(gv.basicAccountsTotalBalance)))
  
  print("Savings Accounts: " + str(gv.savingsAccounts))
  print("Savings Accounts Balance: $" + str(round(gv.savingsAccountsTotalBalance)))
  
  print("Premier Accounts: " + str(gv.premierAccounts))
  print("Permier Accounts Balance: $" + str(round(gv.premierAccountsTotalBalance)) + "\n")



  cp("***EMPLOYEE STATS***", "green")
  print("Total Employees: " + str(gv.totalStaff))
  print("Total Marketing Experts: " + str(gv.marketingStaff))
  print("Total Investment Experts: " + str(gv.investmentExperts))
  print("Total Risk Assessors: " + str(gv.riskAssessors) + "\n")

  if gv.personalLoans == True:
    cp("***Loan Stats***")
    print("Total loans: " + str(round(gv.numberOfLoans)))
    print("Loan Capital: $" + str(round(gv.loanCapital)))
    print("Balance on loan: $" + str(round(gv.onLoanBalance)))
    print("Chance of non-payment: " + str(gv.loanRisk) + "% ")
    print("Chance of non payments leading to default: 1 in " + str(gv.defaultMax))
    print("Balance of all defaulted loans: $" + str(gv.defaultAmount))
  print("Enter 1 to go Home.")
  home = ""
  while home != "1":
    home = input(">> ")

  if home == "1":
    ds.startDay()

