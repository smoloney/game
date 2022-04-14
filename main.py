import random
MONSTERLIST= ["Devil", "Ogre", "Grunt"]
class Player:
    def __init__(self):
        self.hp = 20
        self.strength = 1
        self.level = 0
        self.exp = 0
        self.gold = 0
        self.damage = random.randint(0,3) + self.strength

    def getHP(self):
        return self.hp

    def updateHP(self, value):
        self.hp += value

    def reduceHP(self, value):
        self.hp -= value

    def getLevel(self):
        return self.level

    def updateLevel(self):
        self.level += 1
        self.exp = 0
        self.strength += 2
        self.updateHP(10)
        self.stats()

    def getExp(self):
        return self.exp

    def updateExp(self, value):
        self.exp += value

    def getGold(self):
        return self.gold

    def gainGold(self, value):
        self.gold += value

    def reduceGold(self, value):
        self.gold += value
    
    def getDamage(self):
        return self.damage

    def getStrength(self):
        return self.strength

    def updateStrength(self, value):
        self.strength += value
    
    def stats(self):
        print ("You have ", self.getExp(), " EXP")
        print ("You have ", self.getGold(), " GOLD")
        print ("You have ", self.getStrength(), " STRENGTH")


class Monster:
    def __init__(self, monsterType):
        if(monsterType == "Devil"):
            self.hp = 10
            self.damage = random.randint(2,3)
            self.xp = random.randint(6,10)
        elif (monsterType == "Orge"):
            self.hp = 20
            self.damage = random.randint(0,1)
            self.xp = random.randint(4,6)
        else:
            self.hp = 15
            self.damage = random.randint(0,3)
            self.xp = random.randint(1,4)
        self.monsterType = monsterType

    def getHP(self):
        return self.hp

    def updateHP(self, value):
        self.hp += value

    def reduceHP(self, value):
        self.hp -= value
    
    def getDamage(self):
        return self.damage

    def getMonsterType(self):
        return self.monsterType

    def getXP(self):
        return self.xp
    
def combat(player, monster):
    print ("A wild ", monster.getMonsterType(), " appears! (Hit enter to advance.)")
    whoAttacks = random.randint(0,1)
    while player.getHP() >= 0 and monster.getHP() >= 0:
        if (whoAttacks == 0):
            loseHealth(player, monster)
            print("Player swings sword for ", player.getDamage())
            if(monster.getHP() <=0 ):
                print("The monster has been slain!")
                player.updateExp(monster.getXP())
                player.gainGold(random.randint(5,10))
                if(player.getExp() >= 100):
                    player.updateLevel()
                return True
            print("Player HP: ", player.getHP(), " -- Monster HP: ", monster.getHP(), "\n")
            input()

        if (whoAttacks == 1):
            loseHealth(monster, player)
            if(player.getHP() <=0 ):
                print("You been slain!")
                return False
            input()
            print(monster.getMonsterType() + " swings attacks for ", monster.getDamage())
            print("Player HP: ", player.getHP(), " -- Monster HP: ", monster.getHP())
        whoAttacks = random.randint(0,1)

def loseHealth(attacker, attacked):
    attacked.reduceHP(attacker.getDamage())

def shop(player):
    print("Welcome to the shop")
    print("You currently have ", player.getGold(), " gold.")
    item = str(input('''
    The following items are available:
    1: Health Potion (+10 hp, 5 gold)
    2: Attack boost (+1 strength, 5 gold)
    Please select an item from the menu.
    '''))
    
    if item == "1":
        if player.getGold() >= 5: 
            player.updateHP(10)
        else:
            print("You do not have enough gold for this item!")
    if item == "2":
        if player.getGold() >= 5:
            player.updateStrength(1)
        else:
            print("You do not have enough gold for this item!")
        
    print(player.stats())
    print("Thank you for your business. Please come back again!\n")



def main():

    isAlive = True
    player1 = Player()
    enemy1 = Monster(MONSTERLIST[random.randint(0,2)])
    while(isAlive):
        willShop = str(input("Would you like to shop? (Yes/No) "))
        if willShop.lower() == "yes":
            shop(player1)
            input()
        print()
        isAlive = combat(player1, Monster(MONSTERLIST[random.randint(0,2)]))
        print(player1.stats())

        


    

main()
