import random

class Base:
    def __init__(self, name, sprite, hp=20, atk=3):
        self.name = name
        self.sprite = sprite
        self.hp = hp
        self.atk_damage = atk

    def death(self):
        if self.hp <= 0:
            if self.sprite == 'player':
                print(Self.name, 'has fainted. Do you want to continue?')
            else:
                print(Self.name, 'has been defeated! Do you wish to continue?')

    def attack(self, enemy, name, hit, max_d):
        hit_roll=random.randint(0, 100)
        print(self.name, 'hit roll=', hit_roll)

        if hit >= hit_roll:
            print(self.name, 'used', name, 'successfully.')
            enemy.dmgTaken(self.dmgDealt(max_d))
        else:
            print(self.name, 'used', name, 'and failed')

    def dmgTaken(self, dmg):
        self.hp = self.hp - dmg
        print(self.name, 'took', dmg, 'points of damage!')
        print(self.name, 'has', self.hp, 'hit points left')
        self.death()

    def dmgDealt(self, max_d):
        dmg = random.randint(self.atk_damage, max_d)
        return dmg

    def bag(self, enemy, name, hit, max_d):
        hit_roll=random.randint(0, 100)
        print(self.name, 'hit roll=', hit_roll)

        if hit >= hit_roll:
            print(self.name, 'used', name, 'successfully.')
            enemy.dmgTaken(self.dmgDealt(max_d))
        else:
            print(self.name, 'used', name, 'and failed')

    def Pokemon(self, enemy, name, hit, max_d):
        hit_roll=random.randint(0, 100)
        print(self.name, 'hit roll=', hit_roll)

        if hit >= hit_roll:
            print(self.name, 'used', name, 'successfully.')
            enemy.dmgTaken(self.dmgDealt(max_d))
        else:
            print(self.name, 'used', name, 'and failed')

    def weapon(self, enemy, name, hit, max_d):
        hit_roll=random.randint(0, 100)
        print(self.name, 'hit roll=', hit_roll)

        if hit >= hit_roll:
            print(self.name, 'used', name, 'successfully.')
            enemy.dmgTaken(self.dmgDealt(max_d))
        else:
            print(self.name, 'used', name, 'and failed')




mon_stats = {1: {'name': 'Caterpie', 'hp': 10, 'atk': 1, 'move1': 'tackle', 'move2': 'string shot', 'move3': 'headbutt','move4':'run'},
             2: {'name': 'Rattata', 'hp': 20, 'atk': 2, 'move1': 'tackle', 'move2': 'bite', 'move3': 'headbutt','move4':'run'},
             3: {'name': 'Weedle', 'hp': 30, 'atk': 3, 'move1': 'tackle', 'move2': 'quick attack', 'move3': 'headbutt','move4':'run'}}


move_list = {'tackle': {'hit_rate': 60, 'power': 10},
             'string shot': {'hit_rate': 90, 'power': 5},
             'headbutt': {'hit_rate': 50, 'power': 20},
             'bite': {'hit_rate': 80, 'power': 10},
             'quick attack': {'hit_rate': 90, 'power': 15},
             'run':{'hit_rate':0,'power':0}}

y= 1
player = Base('Chicken (Rod)', 'player')

monster = Base(mon_stats[y]['name'], 'monster')


monster.hp = mon_stats[y]['hp']
monster.atk_damage = mon_stats[y]['atk']


def atk_seq(name, hit, power):
    player.attack(monster, name, hit, power)
    move_choice = ['move1', 'move2', 'move3','move4']
    move_select = random.choice(move_choice)
    monster.attack(player, mon_stats[y][move_select], move_list[mon_stats[y][move_select]]['hit_rate'],
                   move_list[mon_stats[y][move_select]]['power'])

def bag_seq(name, hit, power):
    player.attack(monster, name, hit, power)
    move_choice = ['move1', 'move2', 'move3', 'move4']
    move_select = random.choice(move_choice)
    monster.attack(player, mon_stats[y][move_select], move_list[mon_stats[y][move_select]]['hit_rate'],
                   move_list[mon_stats[y][move_select]]['power'])
def Pokemon_seq(name, hit, power):
    player.attack(monster, name, hit, power)
    move_choice = ['move1', 'move2', 'move3', 'move4']
    move_select = random.choice(move_choice)
    monster.attack(player, mon_stats[y][move_select], move_list[mon_stats[y][move_select]]['hit_rate'],
                   move_list[mon_stats[y][move_select]]['power'])

def weapon_seq(name, hit, power):
    player.attack(monster, name, hit, power)
    move_choice = ['move1', 'move2', 'move3', 'move4']
    move_select = random.choice(move_choice)
    monster.attack(player, mon_stats[y][move_select], move_list[mon_stats[y][move_select]]['hit_rate'],
                   move_list[mon_stats[y][move_select]]['power'])



atk_seq('Thundershock', 30, 10)
bag_seq('bag', 10, 10)
Pokemon_seq('Pokemon', 20,10)
weapon_seq('Using tools!',40,10)



from tkinter import *

root = Tk()
root.minsize(width=300, height=300)

mf = Frame(root)
mf.grid(row=0, column=0)


enemy_hp = IntVar()
enemy_hp.set(200)
Label(mf, textvariable=enemy_hp).grid(row=0, column=1)
Label(mf, text='Monster Hit Points:').grid(row=0, column=0)

result = StringVar()
result.set('You encounter a monster!')
readout = Label(mf, textvariable=result)
readout.grid(row=1, column=0, columnspan=2)

atk = Button(mf, text='attack',command=lambda:atk_seq('Thundershock', 90, 10))
atk.grid(row=2, column=0, columnspan=3, sticky=(N,S,E,W))
bag=Button (mf,text='bag',command=lambda:bag_seq ('quick hit', 50, 10))
bag.grid(row=2, column=1,columnspan=3,sticky=(N,S,E,W))
Pokemon= Button(mf, text='Pokemon',command=lambda:Pokemon_seq('Pokemon', 60,10))
Pokemon.grid(row=3,column=0,columnspan=3,sticky=(N,S,E,W))
weapon=Button(mf,text='Weapon',command=lambda:weapon_seq ('Using tools!',70,10))
weapon.grid(row=3,column=1,columnspan=3,sticky=(N,S,E,W))




root.mainloop()
