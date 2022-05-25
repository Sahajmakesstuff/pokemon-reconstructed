from classes import *

#Empty list for the trainer pokemon
trainer_pokemon=[]

def choose():
    #initializing the 3 pokemon
    firey= pokemon("fire_mon")
    firey.print_everything()

    watery=pokemon("water_mon")
    watery.print_everything()

    leafy=pokemon("grass_mon")
    leafy.print_everything()

    choosing=0

    while choosing==0:

        #taking input
        which_chosen=input("\nEnter The number for which pokemon you want to choose ")

        try:
            #Converting to int
            which_chosen=int(which_chosen)

            #if Firemon
            if which_chosen==1:
                print("\nYou have chosen fire_mon")
                choosing=1
                
                #adding to team
                trainer_pokemon.append(firey)

            #if watermon
            elif which_chosen==2:
                print("\nYou have chosen water_mon")
                choosing=1

                #adding to team
                trainer_pokemon.append(watery)

            #if grassmon
            elif which_chosen==3:
                print("\nYou have chosen grass_mon")
                choosing=1

                #adding to team
                trainer_pokemon.append(leafy)

            #Invalid Answer
            else:
                print("\nInvalid Answer")
        
        #If string is entered
        except ValueError as ve:
            print("\nInvalid Answer")