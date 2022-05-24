# pokemon-reconstructed
An attempt to remake a pokemon-esque game in python

What features do I want?
1. The player should be able to choose from 3 starter pokemon
2. The pokemon will have different base-stats and types
3. The actual stats of a particular mon depend on its base-stats, its IV's or Individual values and its nature
4. The player will be told about the actual stats and nature of the pokemon and they can choose one
5. After this they will be able to fight with one of four trainers who also have 1 pokemon each.
6. Each pokemon will have 4 moves which can be of different types
7. Each move has a base power and if the move is of same type as mon it will get 1.5 times boost called STAB(Same type attack bonus)
8. The AI will be programmed for trainers
9. There should be a system where if a pokemon gets hit it takes damage and its hp decreases.
10. If hp gets to 0, it faints.


BASE STATS:
Each pokemon group will have a set of pre-determined stats. There are 4 different criteria:

HP - the amount of hp a pokemon has
ATTACK - the amount of attack damage a pokemon can do
DEFENCE - the amount of hits it can take
SPEED - how fast it can move


IV's:
These are a range of stats hidden from the player about each specific pokemon's each stat
They range from 0(worst)-31(best)


NATURE:
There are 7 Natures:
1. +Att -Def ---> Lonely
2. +Att -Speed ---> Brave
3. +Def -Att ---> Gentle
4. +Def -Speed ---> Relaxed
5. +Speed -Att ---> Timid
6. +Speed -Def ---> Hasty
7. Neutral ---> Bashful


DETERMINING STATS:

HP - ((Base*2)+(1.5*HP IV))rounded up

Other stats if boosting nature - (((Base*1.5)+(1.2*IV of stat))*1.2)rounded up
            if lowering nature - (((Base*1.5)+(1.2*IV of stat))*0.8)rounded up
            if neutral nature - ((Base*1.5)+(1.2*IV of stat))rounded up
            
            
TRAINER AI:

Each trainer will first decide which of the four moves would do the most damage

If there is no status move:
With a 75% Probability, he will use that move and a 25% chance to use 2nd best move

If There is a status move:
It will see if the opposing pokemon already has that status or not
If yes it will try a different move
If no then with 50% chance it will use that status move


MOVE POWER:

Damage = (((((((2*lvl)/5)+2)*base power of move)/50)+2)*STAB*random)rounded up
random is a value between 0.8 and 1
