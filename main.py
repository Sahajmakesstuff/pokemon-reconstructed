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

        #Invalid Answer
        else:
            print("\nInvalid Answer")
    
    #If string is entered
    except ValueError as ve:
        print("\nInvalid Answer")

#adding random pokemon to party of trainer
trainer_1=[pokemon(random.choice(pokemon_available))]

#Displaying name of pokemon of trainer
print("\nYou are fighting against trainer_1 \nThey sent out a",trainer_1[0].name)

#variable for while loop
done_1=0

while done_1==0: 

    #displaying hp of both pokemon
    print("\nYou are at",trainer_pokemon[0].hp_stat,"HP")
    print("The Opposing pokemon is at",trainer_1[0].hp_stat,"HP")

    #displaying our moves
    print("\nYour moves are:")
    for printing_moves in trainer_pokemon[0].moves:
        print(printing_moves[0])

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
            stab_p=1

            #randomness in deciding damage
            random_var=random.randrange(8,11)
            random_var=random_var/10

            #effectiveness of move variable
            effectiveness=1

            #1/16 chance of crit
            crit_chance=random.randrange(1,17)
            crit_dmg=1

            #var for crits
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
                stab_p=1.5
            
            #if not same type
            else:
                stab_p=1

            #super effective
            if trainer_1[0].typing in strengths[move_info[1]][0]:
                effectiveness=2
                print("The Move was Super Effective")

            #not very effective
            elif trainer_1[0].typing in strengths[move_info[1]][1]:
                effectiveness=0.5
                print("The Move was Not very Effective")

            #damage calculation
            damage=math.ceil(move_info[2]*((trainer_pokemon[0].att_stat/trainer_1[0].def_stat/50)+1)*stab_p*random_var*effectiveness*crit_dmg) 
            
            if damage>=trainer_1[0].hp_stat:
                damage=trainer_1[0].hp_stat

            #Displaying text if it was a crit
            if critical_hit==True:
                print("The Move was a Critical Hit!")

            #displaying amount of damage done
            print("The Move did",damage,"HP of Damage")

            #calculating new HP
            trainer_1[0].hp_stat=trainer_1[0].hp_stat-damage

            #if player wins
            if trainer_1[0].hp_stat<=0:
                done_1=1
                break
            
            #variables for different things to be used
            stab_c=1
            type_e_c=1
            moves_c=[]
            first_choice=""

            #to calc for all 4 moves
            for i in range(0,4):
                est_move_i=trainer_1[0].moves[i]

                #if same type
                if est_move_i[1] == trainer_1[0].typing:
                    stab_c=1.5
                
                #if different type
                else:
                    stab_c=1
                
                #if not very effective
                if est_move_i[1] in strengths[trainer_pokemon[0].typing][0]:
                    type_e_c=0.5    
                
                #if super effective
                elif est_move_i[1] in strengths[trainer_pokemon[0].typing][1]:
                    type_e_c=2
                
                #damage calc for comp to choose
                dmg_move_i=est_move_i[2]*stab_c*type_e_c

                #storing data
                move_i=[dmg_move_i,trainer_1[0].moves[i],stab_c,type_e_c]
                moves_c.append(move_i)
            
            #sorting so strongest moves appear first
            moves_c.sort(reverse = True)

            #fire choice and second choice  
            first_choice=moves_c[0][1]
            sec_choice=moves_c[0][1]
            
            #empty list for move
            move_used=[]

            #random chance to use first or second move
            which_move=random.randrange(1,4)

            #first move
            if which_move != 3:
                move_used=first_choice

            #second move
            else:
                move_used=sec_choice
            
            #displaying move used
            print("\nThe Opposing pokemon used",move_used[0])

            #random chance between 0.8 and 1
            ran_c=random.randrange(8,11)
            ran_c=ran_c/10

            #crit chance
            crit_c=random.randrange(1,17)
            crit_dmg_c=1

            #if crit
            if crit_c==10:
                crit_dmg_c=1.5
                print("\nThe Move was a Critical Hit")
            
            #if not crit
            else:
                crit_dmg_c=1

            #super effective
            if moves_c[0][3]==2:
                print("The Move was super Effective")

            #not very effective
            elif moves_c[0][3]==0.5:
                print("The Move was not very effective")

            #damage calc
            damage_c=math.ceil(moves_c[0][0]*ran_c*crit_dmg_c)

            #cap on maximum damage
            if damage_c>=trainer_pokemon[0].hp_stat:
                damage_c=trainer_pokemon[0].hp_stat
            
            #displaying damage
            print("The Move did",damage_c,"HP of Damage")

            #changing HP
            trainer_pokemon[0].hp_stat=trainer_pokemon[0].hp_stat-damage_c

            #if computer wins
            if trainer_pokemon[0].hp_stat<=0:
                done_1=2
                break
            
        #number greater than 4
        else:
            print("Invalid Move")

    #string entered
    except ValueError as ve:
        print("Invalid Move")
    
#you won
if done_1==1:
    print("\nCongrats!! \nYou Defeated Trainer_1")

#you lost
elif done_1==2:
    print("\nSorry! You lost to trainer_1")


