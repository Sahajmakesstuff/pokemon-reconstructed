#importing modules
import random
import math

#list of natures
natures=["lonely","brave","gentle","relaxed","timid","hasty","bashful"]

#class for all pokemon
class pokemon:

    #boosts in stats due to nature
    att_b=1
    def_b=1
    spd_b=1

    def __init__(self,whichmon):

        #taking input of which pokemon it is
        self.name=whichmon

        #fire_mon's info
        if self.name=="fire_mon":
            self.base_hp=100
            self.base_att=85
            self.base_def=60
            self.base_spd=115
            self.typing="fire"

        #water_mon's info
        elif self.name=="water_mon":
            self.base_hp=120
            self.base_att=70
            self.base_def=100
            self.base_spd=70
            self.typing="water"

        #grass_mon's info
        elif self.name=="grass_mon":
            self.base_hp=50
            self.base_att=120
            self.base_def=100
            self.base_spd=90
            self.typing="grass"
        
        self.hp_IV=random.randrange(0,32)
        self.att_IV=random.randrange(0,32)
        self.def_IV=random.randrange(0,32)
        self.spd_IV=random.randrange(0,32)
        self.nature=random.choice(natures)
        self.calc_boosts()
        self.calc_stats()        
    
    def calc_boosts(self):
        if self.nature=="lonely":
            self.att_b=1.2
            self.def_b=0.8
            
        elif self.nature=="brave":
            self.att_b=1.2
            self.spd_b=0.8

        elif self.nature=="gentle":
            self.def_b=1.2
            self.att_b=0.8

        elif self.nature=="relaxed":
            self.def_b=1.2
            self.spd_b=0.8

        elif self.nature=="timid":
            self.spd_b=1.2
            self.att_b=0.8
            
        elif self.nature=="hasty":
            self.spd_b=1.2
            self.def_b=0.8

    def calc_stats(self):
        self.hp_stat=math.ceil(self.base_hp*3+0.15*self.hp_IV)
        self.att_stat=math.ceil((self.base_att*2+0.1*self.att_IV)*self.att_b)
        self.def_stat=math.ceil((self.base_def*2+0.1*self.def_IV)*self.def_b)
        self.spd_stat=math.ceil((self.base_spd*2+0.1*self.spd_IV)*self.spd_b)
    
    def print_everything(self):
        print("\n",self.name)
        print("The Type is",self.typing)
        print("\nThe HP is",self.hp_stat)
        print("The Attack is",self.att_stat)
        print("The Defense is",self.def_stat)
        print("The Speed is",self.spd_stat)
        print("The Nature is",self.nature)
        

