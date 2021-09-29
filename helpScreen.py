import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Strings as myStrings
import dayStart as ds
import hireStaff as hs
import getCustomers as gc
import improveBank as ib
import loanManagement as Loan

from termcolor import cprint as cp
from colorama import *

options = ["1", "2", "3"]
def helpOptions(lastScreen) :
  replit.clear()
  selectedOption = 0
  gm.typePrint("Welcome to the help page.")
  gm.typePrint(myStrings.pleaseChoose)
  
  print("1. Go back to previous screen")
  print("2. Game Basics")
  print("3. FAQ")
  

  while selectedOption not in options:
    selectedOption = input(">> ")

  if selectedOption == "1":
    back(lastScreen)

  if selectedOption == "2":
    basics(lastScreen)

  if selectedOption == "3":
    faq(lastScreen)

def back(lastScreen):
  if lastScreen == 1:
    ds.startDay()
  
  if lastScreen == 2:
    hs.newStaff()
  
  if lastScreen == 3:
    gc.getCustomers()
  
  if lastScreen == 4:
    ib.improvements()

  if lastScreen == 5:
    loans.loanMenu()

def basics(lastScreen):
  replit.clear()

  cp("Welcome to the Game basics", "green")

  cp("\n What this game is about.", "green")
  print("This game is a text based Bank management Tycoon style game. You are the owner and CEO of your own bank and need to make it successful. If you go bakrupt the game ends. There is no specific win condition the goal is to keep the bank going as long as possible")
  print("\n There are a number of random events that can occur that will help or hinder you. These events become more common as you buy more branches reaching their most frequent when you have 100 branches. Some random events also have other requirements before they can occur such as minimum customer limits.")
  print("\n I have tried to balance the game to give the player a challenge but ultimately keeping the odds in their favour. Because of this negative random events are more powerful than positive ones.")

  cp("\n Gameplay", "green")
  print("You start the game with $1000 and daily costs set at $150 per branch. You need to gain customers to make money. The best place for this especially for the first few days is the get customers screen. You can also randomly gain customers at the end of each day and later hire staff that will automarically get customers each day.")
  print("You start with 1 action per day and 1 branch. You can buy more branches and actions in the Bank Improvements screen. Your bank does not initially start with the ability to offer loans but this can also be unlocked from the bank Improvements Screen")
  print("Your main source of income especially before you unlock loans will be investment income from customer accounts. This is also the risky part of running the bank. You have guaranteed customers set rate of intrest depending on their account type but the amount you make from investments varies. This means that you can and sometimes will make less from investments than you pay to customers and need to ensure you always have a buffer of cash on had to deal with this.")


  print("\n Would you like to return to the help menu? [y/n]")
  answer = gm.getAnswer()

  if answer == "y":
    helpOptions(lastScreen)

  else:
    basics(lastScreen)

def faq(lastScreen):
  replit.clear()

  cp("Welcome to the FAQ", "green")
  
  cp("\n What is the goal of the game?", "green")
  print("The goal of the game is to expand your bank to make as much money as you can and avoid bankruptcy. Although there is no specific win condition if you go below $0 you lose.")

  cp("\n I don't like the slow typed out text, can i turn it off?", "green")
  print("Yes you can from the home screen you can enter u to go to the User Settings where the text speed can be changed.")

  cp("\n How many random events are there?", "green")
  print("Currently there are 18 random events that of which a maximum of 1 can occur each day. In addition to this there are 2 other events that have seperate probability calculations that can occur alongside the other random events and each other. The 2 extra events simply cover random customer gain and loss.")

  cp("\n How does each customer account work", "green")
  print("There are 3 types if account Basic, Savings and Premier. Premier accounts have the highest intrest rate for customers but they pay you $10 each day for each account. Baisc accounts have the lowest intrest rate.")
  print("Basic accounts make 0.02% interest per day")
  print("Savings accounts make 0.04% interest per day")
  print("Premier accounts make 0.07% interest per day")
  print("You will make between 0.01% and 0.1% from all accounts in investments each day. Any day above 0.08% intrest guarantees you profit overall. Days below this can cost you money if account intrest is higher than the investment income and premier account fees.")
  
  print("\n Would you like to return to the help menu? [y/n]")

  answer = gm.getAnswer()

  if answer == "y":
    helpOptions(lastScreen)

  else:
    faq(lastScreen)