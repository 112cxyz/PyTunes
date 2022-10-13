import os
import time
#import pytunesmanager as ptmgr
def clear():
  os.system("clear")
clear()

def pyinfo():
  print("PyTunes: Version: 0.0.1 Channel: Canary\n")

def runtour():
  print("In PyTunes we have 2 Main Functions: \n\nLibrary Management\nMusic Playing\nFor Music Playback & Library Management you can select it in the main menu")
  print("Would you like to go to the main menu?")
  mainmenu = input("\nyes/no: >>> ")
  if mainmenu.lower() == "yes":
    menu(True)
  elif mainmenu.lower() == "no":
    print("There is nothing else to do so goodbye?")
    exit()



def tourask():
  tour = input("\nyes/no: >>> ")
  if tour.lower() == "yes":
    clear()
    runtour()
  elif tour.lower() == "no":
    print("Alright!")

  else:
    print("That Wasnt A Option ):")
    time.sleep(3)
    os.system("clear")
    menu()

def showmusicmenu():
  import pytunesmanager as ptmgr
  import pytunesplayer as ptplr
  clear()
  pyinfo()
  ptplr.librarylist()
  input("Press Enter To Continue")

def musicmenu():
    import pytunesmanager as ptmgr
    import pytunesplayer as ptplr
    clear()
    pyinfo()
    ptplr.librarylist()
    print("Select Song From List:")
    songid = int(input("Song ID: >>> "))
    try:
      clear()
      pyinfo()
      ptplr.playsong(songid-1)
    except:
      print("Something went wrong try again.")
      time.sleep(3)
      clear()
      menu()

def librarymenu():
  import pytunesmanager as ptmgr
  clear()
  pyinfo()
  ptmgr.addsongmenu()
  menu()
  import pytunesplayer as ptplr


def menu(aftertour=False):
  pyinfo()
  if aftertour==False:
    if os.path.exists("Library/Library.json") == False:
      print("Welcome To PyTunes!\n")
      print("PyTunes is a Python based music player for Unix!\nWould You Like A Tour?")
      tourask()
  print("Please Select:\n\n1 Play Music:\n2 Manage Library:\n3 Show Library:")
  menuselect = input("1/2/3: >>>")
  if menuselect == "1":
    musicmenu()
  elif menuselect == "2":
    librarymenu()
  elif menuselect == "3":
    showmusicmenu()
    menu()
  else:
    print("Sorry Thats Not A Option ):")
    
    

menu()
    

  
    
