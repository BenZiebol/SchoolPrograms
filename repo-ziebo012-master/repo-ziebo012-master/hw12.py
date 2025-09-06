#Adventurer=================================
# Purpose: Creates an adventurer and stores various details about them
# Instance variables: 
# name-the name of person
# level-the level of person
# strength-the strength of person
# speed-the speed of person
# power-the power of person
# Methods: __init__ initializes the variables
# __repr__ returns the proper formating
# attack attack the target
#==========================================
class Adventurer:
    def __init__(self,name,level,strength,speed,power):
        self.name=str(name)
        self.level=int(level)
        self.strength=int(strength)
        self.speed=int(speed)
        self.power=int(power)
        self.HP=int(level*6)
        self.hidden=False
    def __repr__(self):
        return self.name+' - HP: '+str(self.HP)
    def attack(self,target):
        if not target.hidden:
            saying=self.name+' attacks '+target.name+' for '+str(self.strength+4)+' damage'
            target.HP-=self.strength+4
        else:
            saying=self.name+" can't see "+target.name
        print(saying)

#Thief=================================
# Purpose: Creates a thief and stores various details about them
# Instance variables: 
# name-the name of person
# level-the level of person
# strength-the strength of person
# speed-the speed of person
# power-the power of person
# Methods: __init__ initializes the variables
# attack attack the target
#==========================================
class Thief(Adventurer):
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.HP=8*level
        self.hidden=True
    def attack(self,target):
        if self.hidden:
            print(self.name+' sneak attacks '+target.name+' for '+str((self.speed+self.level)*5)+' damage')
            target.HP-=(self.speed+self.level)*5
            self.hidden=False
            target.hidden=False
        else:
            Adventurer.attack(self,target)

#mage=================================
# Purpose: Creates a mage and stores various details about them
# Instance variables: 
# name-the name of person
# level-the level of person
# strength-the strength of person
# speed-the speed of person
# power-the power of person
# Methods: __init__ initializes the variables
# attack attack the target
#==========================================       
class Mage(Adventurer):
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.fireballs_left=power
    def attack(self,target):
        if self.fireballs_left>0:
            self.fireballs_left-=1
            target.hidden=False
            target.HP-=self.level*3
            print(self.name+' casts fireball on '+target.name+' for '+str(self.level*3)+' damage')
        else:
            Adventurer.attack(self,target)

#ninja=================================
# Purpose: Creates a ninja and stores various details about them
# Instance variables: 
# name-the name of person
# level-the level of person
# strength-the strength of person
# speed-the speed of person
# power-the power of person
# Methods:
# attack attack the target
#==========================================    
class Ninja(Thief):
    def attack(self,target):
        Thief.attack(self,target)
        self.hidden=True
        self.HP+=self.level

#wizard=================================
# Purpose: Creates a wizard and stores various details about them
# Instance variables: 
# name-the name of person
# level-the level of person
# strength-the strength of person
# speed-the speed of person
# power-the power of person
# Methods: __init__ initializes the variables
#==========================================
class Wizard(Mage):
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.HP=level*4
        self.fireballs_left=power*2

def battle(player_list, enemy_list):
    while len(player_list)>0 and len(enemy_list)>0:
        print('----------Player Turn----------')
        print('Your team:')
        for i in player_list:
            print(i)
        print()
        
        for i in player_list:
            for j in range(len(enemy_list)):
                print('Enemy '+str(j+1)+': '+str(enemy_list[j]))
            battle_target=int(input('Choose a target for '+i.name+': '))-1
            i.attack(enemy_list[battle_target])
            if enemy_list[battle_target].HP<=0:
                print(str(enemy_list[battle_target].name)+' was defeated!')
                enemy_list.remove(enemy_list[battle_target])
                if len(enemy_list)<1:
                    print('You win!')
                    return player_list
            print()
        print('----------Enemy Turn----------')
        for i in range(len(enemy_list)):
            battle_target=player_list[0]
            for j in player_list:
                if j.HP<battle_target.HP:
                    battle_target=j
            enemy_list[i].attack(battle_target)
            if battle_target.HP<=0:
                print(str(battle_target.name)+' was defeated!')
                player_list.remove(battle_target)
                if len(player_list)<1:
                    print('You lose!')
                    return enemy_list
        print()
            
