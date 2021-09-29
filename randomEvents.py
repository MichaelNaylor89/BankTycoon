import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Variables as gv
import MyGlobal.Strings as myStrings
import getCustomers as gc
import hireStaff as hs
import statsPage as stats
import helpScreen
import improveBank as ib
import dayStart as ds

from termcolor import cprint as cp
from colorama import *
global typeSpeed

def eventChance():
  dailyCustomerLoss()
  dailyCustomerGain()
  doEvent = random.randint(1,100)
  if(doEvent > gm.noEventChance()):
    
    whichEvent()
    time.sleep(1.5)

def dailyCustomerGain():
  gain = 0
  gain = random.randint(1,10)
  if gain < 4:
    amount = gv.currentDay * gain
    i = 0
    while i < amount:
      gc.addNewCustomer()
      i += 1
    gv.customers += amount
    gm.typePrint(str(amount) + " customers have joined your bank. They heard about your bank from their friends and family")

def dailyCustomerLoss():
  if gv.customers > 1000:
    lose = 0
    lose = random.randint(1,10)
    if lose == 1:
      randomLoss = random.randint(1, round((gv.customers/100)))
      i = 0
      while i < randomLoss:
        lostCustomer()
        i += 1
      gv.customers -= randomLoss
      gm.typePrint(str(randomLoss) + " customers left your bank to join a competitor today.")

def whichEvent():
  event = 0
  event = random.randint(1,21)
  
  if event % 2 == 0:
    improveChance = random.randint(1,100)
    if improveChance <= gv.fixerChance:
      event += 1

  if event == 1:
    stolenCustomers()
  
  if event == 2:
    highProfileInfluencer()

  if event == 3:
    insurancePriceHike()
  
  if event == 4:
    utilityDiscount()
  
  if event == 5:
    staffWageIncrease()
  
  if event == 6:
    accountUpgrade()

  if event == 7:
    branchUpdate()

  if event == 8:
    freeBranch()

  if event == 9:
    smallMarketCrash()
  
  if event == 10:
    sellDefaultAccounts()
  
  if event == 11:
    unhappyCelebrity()

  if event == 12:
    smallCompetitorShutdown()
  
  if event == 13:
    stolenCustomersBetterDeal()
  
  if event == 14:
    bigCompetitorShutdown()
  
  if event == 15:
    stolenCustomersBestDeal()

  if event == 16:
    veryBigCompetitorShutdown()
  
  if event == 17:
    marketingWalkout()
  
  if event == 18:
    referAFriendEmployeeGain()
  
  if event == 19:
    shadyPolitics()
  

##### random events #####

### positive ###
def highProfileInfluencer():
  newCustomerAmount = round(gv.branches + round(gv.customers/100))

  i = 0
  while i < newCustomerAmount:
    gc.addNewCustomer()
    i += 1
  gv.customers += newCustomerAmount
  cp("A high profile celebrity has recommended your bank on social media you have gained: " + str(newCustomerAmount) + " new customers", "green")

def utilityDiscount():
  gv.baseCostPerBranch *= 0.95

  cp("You have recieved a letter from one of your utility providers informing you of a loyalty discount you are now eligible for. Your base daily costs for each branch have decreased by 5% to $" + str(gv.baseCostPerBranch), "green")

def accountUpgrade():
  if gv.customers > 100:
    newAccs = round(gv.branches + round(gv.customers/100))
    gv.premierAccounts += newAccs
    i = 0
    while i < newAccs:
      gv.premierAccountsTotalBalance += gm.accountAmount(2)
      i += 1
    
    cp("Due to a great promotion for existing customers from your staff " + str(newAccs) + " customers have opened premier accounts and moved savings from other banks to yours.", "green")

def freeBranch():
  if gv.branches > 10:
    newBranches = random.randint(1,round(gv.branches/10))
    gv.branches += newBranches
  
  cp("You have merged with a smaller competitor who was struggling. You have aquired " + str(newBranches) + " new branches at no cost and without increasing the cost of future branches.", "green")

def sellDefaultAccounts():
  if gv.defaultAmount > 100000:
    profit = gv.defaultAmount / 10
    gv.cash += (profit)
    gv.defaultAmount = 0
    cp("A collections agency has offered to buy all of your default loan accounts at 10% of their value. As you did not have the resources to chase these accounts any longer you happily sell them on. You have made $" + str(round(profit)) + " from this deal", "green")

def smallCompetitorShutdown():
  newCustomerAmount = round(gv.branches + round(gv.customers/100))

  i = 0
  while i < newCustomerAmount:
    gc.addNewCustomer()
    i += 1
  gv.customers += newCustomerAmount
  cp("A small rival bank has gone out of business and you have taken all of their customers: " + str(newCustomerAmount) + " new customers", "green")

def bigCompetitorShutdown():
  if gv.customers > 50000:
    newCustomerAmount = round(gv.branches + round(gv.customers/10))

    i = 0
    while i < newCustomerAmount:
      gc.addNewCustomer()
      i += 1
    gv.customers += newCustomerAmount
    cp("A large rival bank has gone out of business and you have taken all of their customers: " + str(newCustomerAmount) + " new customers", "green")

def veryBigCompetitorShutdown():
  if gv.customers > 500000:
    newCustomerAmount = round(gv.branches + round(gv.customers * 1.35))

    i = 0
    while i < newCustomerAmount:
      gc.addNewCustomer()
      i += 1
    gv.customers += newCustomerAmount
    cp("A huge rival bank has gone out of business and you have taken all of their customers: " + str(newCustomerAmount) + " new customers", "green")

def referAFriendEmployeeGain():
  if gv.branches > 100:
    newStaff = round(gv.branches/10)
    marketingStaff += newStaff
    cp("A very successful refer a friend scheme has gained you " + str(newStaff) + " new Marketing Experts with no recruitment cost", "green")

### negative###

def stolenCustomers():
  if gv.customers > 100:
    lossAmount = round(gv.customers/100)
    cp("Oh no a rival bank has intoduced a new customer deal specifially targeting your customers. You have lost " + str(lossAmount) + " customers.", "red")
    i = 0
    while i < lossAmount:
      lostCustomer()
      i += 1
    gv.customers -= lossAmount

def lostCustomer():
  numAccounts = random.randint(1, 3)

  if numAccounts == 1:
    gv.basicAccounts -= 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts

    gv.basicAccountsTotalBalance -= gm.accountAmount(numAccounts)

  if numAccounts == 2:
    gv.basicAccounts -= 1
    gv.savingsAccounts -= 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts

    gv.basicAccountsTotalBalance -= gm.accountAmount(numAccounts)
    gv.savingsAccountsTotalBalance -= gm.accountAmount(numAccounts)


  if numAccounts == 3:
    gv.savingsAccounts -= 1
    gv.premierAccounts -= 1
    gv.totalAccounts = gv.basicAccounts + gv.savingsAccounts + gv.premierAccounts
    
    gv.savingsAccountsTotalBalance -= gm.accountAmount(numAccounts)
    gv.premierAccountsTotalBalance -= gm.accountAmount(numAccounts)

def insurancePriceHike():
  gv.baseCostPerBranch *= 1.15

  cp("Letter from your utility providers your bills have increased. Your base daily costs for each branch has increased by 15% to $" + str(gv.baseCostPerBranch), "red")

def staffWageIncrease():
  if gv.totalStaff > 25:
    gv.marketingWages *= 1.075
    gv.investorWages *= 1.075
    gv.raWages *= 1.075

    cp("Your employee union have negotiated a price increase to bring your staff wages in line with other banks. All wages for current and future have increased by 7.5%", "red")

def branchUpdate():
  if gv.customers > 100:
    cost = gv.branches * (gv.baseCostPerBranch * 10)

    gv.cash -= cost
    cp("Your customers have complained that your branches look dated. Your PR team have advised you that this may be putting off potential customers. You have spent $" + str(cost) + " to refurbish your branches.", "red" )

def smallMarketCrash():
  if gv.customers > 2500:
    gv.baseCostPerBranch *= 1.05
    cp("A small market crash caused you to lose a lot of money from both your own current cash and customer accounts. Luckily your insurance covers this kind of event but your insurance costs increasing your daily costs poer branch to $" + str(round(gv.baseCostPerBranch)), "red")

def unhappyCelebrity():
  if gv.customers > 1000:
    amount = random.randint(10 ,round(gv.customers/100))
    gv.customers -= amount
    gv.cash -= 1000
    cp("A celebrity has complained about your banks customers service on social media. You have lost " + str(amount) + " customers and have paid $1000 to provide enhanced customer service training in the branch that was complained about.", "red")

def stolenCustomersBetterDeal():
  if gv.customers > 100000:
    lossAmount = round(gv.customers/20)
    cp("Oh no a rival bank has intoduced a popular new customer deal specifially targeting your customers. You have lost " + str(lossAmount) + " customers.", "red")
    i = 0
    while i < lossAmount:
      lostCustomer()
      i += 1
    gv.customers -= lossAmount

def stolenCustomersBestDeal():
  if gv.customers > 1000000:
    lossAmount = round(gv.customers/10)
    cp("Oh no a rival bank has intoduced a hugely popular new customer deal specifially targeting your customers. You have lost " + str(lossAmount) + " customers.", "red")
    i = 0
    while i < lossAmount:
      lostCustomer()
      i += 1
    gv.customers -= lossAmount
  
def marketingWalkout():
  if gv.marketingStaff > 20:
    lossAmount = round(gv.marketingStaff/20) + 1
    gv.marketingStaff -= lossAmount
    cp("You have averted a strike by negotiating brilliantly with the staff union however some staff are still unhappy. You have lost " + lossAmount + " Marketing Staff")

def shadyPolitics():
  if gv.cash > 10000000:
    bribe = random.randint(1000, (gv.cash/10))
    gv.cash -= bribe
    cp("Oh no a shady politician threatened to push for laws increasing taxes on banks unless you bribed him. You obliged and paid him $" + bribe + " but you know this won't be the last bribe you have to pay out.")