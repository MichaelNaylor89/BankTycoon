import random, replit, time, sys
import MyGlobal.Methods as gm
import MyGlobal.Variables as gv
import MyGlobal.Strings as myStrings
import dayStart as ds

from termcolor import cprint as cp
from colorama import *

options = ["1", "2"]
speedOptions = ["1", "2", "3", "4"]

def userOptions():
  replit.clear()
  print("Welcome to the settings screen \n")


  cp("Options", "green")
  gm.typePrint(myStrings.pleaseChoose)
  print("1. Back to home Screen")
  print("2. Type Speed")
  
  chosenAction = ""

  while chosenAction not in options:
      chosenAction = input(">> ")

  if chosenAction == "1":
    ds.startDay()
  
  if chosenAction == "2":
    changeTypeSpeed()

def changeTypeSpeed():
  replit.clear()
  print("Welcome to the settings screen \n")

    
  cp("Type speed options", "green")
  print("Current speed setting: " + str(gv.currentSpeedSetting))
  gm.typePrint(myStrings.pleaseChoose)

  print("1. Go back")
  print("2. Instant")
  print("3. Fast")
  print("4. slow")

  speedChoice = ""
  while speedChoice not in speedOptions:
    speedChoice = input(">> ")
    
  if speedChoice == "1":
    userOptions()
    
  if speedChoice == "2":
    gm.typePrint("Changing speed to instant...")
    gv.typeSpeed = 0
    gv.currentSpeedSetting = "instant"
    time.sleep(1.5)
    userOptions()

  if speedChoice == "3":
    gm.typePrint("Changing speed to fast...")
    gv.typeSpeed = 0.01
    gv.currentSpeedSetting = "fast"
    time.sleep(1.5)
    userOptions()

  if speedChoice == "4":
    gm.typePrint("Changing speed to slow...")
    gv.typeSpeed = 0.05
    gv.currentSpeedSetting = "slow"
    time.sleep(1.5)
    userOptions()
