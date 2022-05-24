#importing module
from classes import *

#initializing the 3 pokemon
firey= pokemon("fire_mon")
firey.print_everything()

watery=pokemon("water_mon")
watery.print_everything()

leafy=pokemon("grass_mon")
leafy.print_everything()

choosing=0

while choosing==0:
    which_chosen=input("\nEnter The number for which pokemon you want to choose ")

    try:
        which_chosen=int(which_chosen)

        if which_chosen==1:
            print("You have chosen fire_mon")
            choosing=1

        elif which_chosen==2:
            print("You have chosen water_mon")
            choosing=1

        elif which_chosen==3:
            print("You have chosen grass_mon")
            choosing=1

        else:
            print("Invalid Answer")
        
    except ValueError as ve:
        print("Invalid Answer")

input("\nPress Enter to Exit")
