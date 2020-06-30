from abc import ABC, abstractmethod
import random
import Items


class Hero(ABC):
    """Abstract hero class"""
    name = ''
    hp = 30
    weapons_list = {'sword': 10}
    summary_arrows = 0
    monster_dead = 0

    def take_weapon(self, weapon):
        """take a new weapom"""
        new_weapons_list = self.weapons_list
        print(new_weapons_list)
        new_weapons_list[weapon[0]] = weapon[1]
        self.weapons_list = new_weapons_list

    def heal(self, healing_points: int):
        """restore some hp"""
        self.hp = self.hp + healing_points

    def hero_attack(self, weapon_list=weapons_list):
        print('Выберите тип атаки . Вам доступны атаки {}'.format(list(weapon_list.keys())))




    @abstractmethod
    def special_class_skill(self, enemy_attack):
        luck = random.choice([True, False])
        pass


class Warrior(Hero):
    """Warrior class"""

    def special_class_skill(self, enemy_attack: tuple):
        if enemy_attack[1] == 'melee':
            luck = random.choice([True, False])
            if luck == True:
                print('Вы заблокировали атаку ближнего боя')
                return 0
            else:
                print('Вы не смогли заблокировать атаку')
                return enemy_attack[0]
        else:
            print('Особая способность неактивная против данного противника')
            return enemy_attack[0]


class Archer(Hero):
    """Archer class"""

    def special_class_skill(self, enemy_attack: tuple):
        if enemy_attack[1] == 'range':
            luck = random.choice([True, False])
            if luck == True:
                print('Вы заблокировали атаку ближнего боя')
                return 0
            else:
                print('Вы не смогли заблокировать атаку')
                return enemy_attack[0]
        else:
            print('Особая способность неактивная против данного противника')
            return enemy_attack[0]
        pass


class Mage(Hero):
    """mage class"""

    def special_class_skill(self, enemy_attack: tuple):
        if enemy_attack[1] == 'spell':
            luck = random.choice([True, False])
            if luck == True:
                print('Вы заблокировали атаку ближнего боя')
                return 0
            else:
                print('Вы не смогли заблокировать атаку')
                return enemy_attack[0]
        else:
            print('Особая способность неактивная против данного противника')
            return enemy_attack[0]

a = Warrior()
print(a.weapons_list)
a.take_weapon(('Bow',5))
print(a.weapons_list)
a.hero_attack()