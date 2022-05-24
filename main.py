#importing module
import random 
import math
from classes import *
from types import *

#initializing the 3 pokemon
firey= pokemon("fire_mon")
firey.print_everything()

watery=pokemon("water_mon")
watery.print_everything()

leafy=pokemon("grass_mon")
leafy.print_everything()

#Empty list for the trainer pokemon
trainer_pokemon=[]

#list of available pokemon for computer
pokemon_available=["fire_mon","water_mon","grass_mon","rock_mon","ice_mon","steel_mon","elec_mon","normal_mon"]

#variable for when to finish choosing
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

        else:
            print("\nInvalid Answer")
    
    #If string is entered
    except ValueError as ve:
        print("\nInvalid Answer")

#adding random pokemon to party of trainer
trainer_1=[pokemon(random.choice(pokemon_available))]

#Displaying name of pokemon of trainer
print("\nYou are fighting against trainer_1 \nThey sent out a",trainer_1[0].name)

#displaying our moves
print("\nYour moves are:")
for printing_moves in trainer_pokemon[0].moves:
    print(printing_moves[0])

#variable for while loop
done_1=0

while done_1==0:

    #displaying hp of opposing pokemon
    print("The Opposing pokemon is at",trainer_1[0].hp_stat,"HP")

    #taking input for move
    move_chosen=input("\nWhich Move Would you like to choose? \n(Answer with 1,2,3 or 4) ")

    try:
        #converting input to int
        move=int(move_chosen)

        #if valid 
        if move>0 and move<5:

            #reaches the move
            move_info=trainer_pokemon[0].moves[move-1]

            #name of move
            act_move=move_info[0]

            #displaying name of move used
            print("\n",trainer_pokemon[0].name,"used",act_move)

            #same type attack bonus var
            stab=1

            #randomness in deciding damage
            random_var=random.randrange(8,11)
            random_var=random_var/10

            #effectiveness of move variable
            effectiveness=1

            #1/16 chance of crit
            crit_chance=random.randrange(1,17)
            crit_dmg=1

            critical_hit=False

            #if it is a crit
            if crit_chance==5:
                crit_dmg=1.5
                critical_hit=True

            #if not a crit
            else:
                crit_dmg=1

            #if same type
            if trainer_pokemon[0].typing==move_info[1]:
                stab=1.5
            
            #if not same type
            else:
                stab=1

            #super effective
            if trainer_1[0].typing in strengths[move_info[1]][0]:
                effectiveness=2
                print("The Move was Super Effective")

            #not very effective
            elif trainer_1[0].typing in strengths[move_info[1]][1]:
                effectiveness=0.5
                print("The Move was Not very Effective")

            #neutral
            else:
                effectiveness=1

            #damage calculation
            damage=math.ceil(move_info[2]*((trainer_pokemon[0].att_stat/trainer_1[0].def_stat/50)+1)*stab*random_var*effectiveness*crit_dmg) 
            
            #Displaying text if it was a crit
            if critical_hit==True:
                print("\nThe Move was a Critical Hit!")

            #displaying amount of damage done
            print("The Move did",damage,"HP of Damage")

            #calculating new HP
            trainer_1[0].hp_stat=trainer_1[0].hp_stat-damage

            #if player wins
            if trainer_1[0].hp_stat<=0:
                done_1=1
        
        #number greater than 4
        else:
            print("Invalid Move")

    #string entered
    except ValueError as ve:
        print("Invalid Move")

#you won
if done_1==1:
    print("\nCongrats!! \nYou Defeated Trainer_1")


