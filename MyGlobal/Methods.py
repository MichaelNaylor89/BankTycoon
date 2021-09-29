import random, replit, time, sys
import MyGlobal.Variables as gv

from termcolor import cprint as cp
from colorama import *

ynOptions = ["y", "n"]

def typePrint(string):
  for char in string:
    time.sleep(gv.typeSpeed)
    sys.stdout.write(char)
    sys.stdout.flush()
  print('\n')

def displayStats():
  cp("Welcome to day " + str(gv.currentDay) + " of running " + gv.bankName, "green")
  print("You have " + str(gv.branches) + " branches and " + str(gv.customers) + " customers")
  print("Customers have a total of $" + str(round(totalAccBalance())) + " across all accounts with you")
  print("You currently have: $" + str(round(gv.cash)) + " available to spend")
  print("You have " + str(gv.dailyActions) + " action(s) still available for today")
  cp("Enter h for help, o for options or s to view your banks stats \n", "green")

def customerAmount(multiplyer):
  minCustomers = gv.baseNewCustMin * multiplyer * gv.bankPopularity * gv.branches
  maxCustomers = gv.baseNewCustMax * multiplyer * gv.bankPopularity * gv.branches
  newCustomers = random.randint(minCustomers, maxCustomers) + gv.currentDay
  return newCustomers

def accountAmount(extraMulti):
  customerWealthMulti = random.randint(1,100)
  
  balance = (customerWealthMulti * gv.areaWealthMulti) * extraMulti

  return balance

def noEventChance():
  if gv.branches < 100:
    return 100 - gv.branches
  else:
    return 1

def totalAccBalance():
  return round(gv.basicAccountsTotalBalance + gv.savingsAccountsTotalBalance + gv.premierAccountsTotalBalance)

def getAnswer():
  answer = ""
  while answer not in ynOptions:
    answer = input(">> ")
  return answer

def continuePrompt():
  continueOptions = ["c", "C"]
  cp("Enter c to continue", "green")
  advance = ""
  while advance not in continueOptions:
    advance = input(">> ")