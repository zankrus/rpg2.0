from abc import ABC, abstractmethod
import random
import Items


class Hero(ABC):
    """Abstract hero class"""
    name = ''
    hp = 30
    weapons_list = {'sword': 10}
    summary_arrows = 2
    monster_dead = 0
    save_hp = None
    save_weapons_list = None
    save_summary_arrows = 0
    save_monster_dead = 0
    game_saved = False

    def take_weapon(self, weapon):
        """take a new weapom"""
        while True:
            choice = input('Введите 1 ,чтобы поднять меч '
                             'или 2, чтобы пройти мимо : ')
            if choice == '1':
                new_weapons_list = self.weapons_list
                new_weapons_list[weapon[0]] = weapon[1]
                self.weapons_list = new_weapons_list
                break
            elif choice == '2':
                print('Вы прошли мимо')
                break
            else:
                print('Вы ввели неверное значение. Введите 1 или 2')


    def heal(self, healing_points: int):
        """restore some hp"""
        self.hp = self.hp + healing_points

    def hero_attack(self, weapon_list=weapons_list):
        temp = {}
        for i in range(len(weapon_list)):
            print('Нажмите {0}, чтобы выбрать {1}'.format(i + 1, list(weapon_list)[i]))
            temp[i + 1] = list(weapon_list)[i]
        choice = input('Введите номер оружия: ')
        while True:
            if 0 < int(choice) < len(temp) + 1:
                if temp[int(choice)] == 'bow':
                    if self.summary_arrows > 0:
                        self.summary_arrows -= 1
                        print('Вы выбрали {}'.format(temp[int(choice)]))
                        print('У вас осталось стрел  {}'.format(self.summary_arrows))
                        print(weapon_list[temp[int(choice)]])
                        return weapon_list[temp[int(choice)]]
                    else:
                        print('У вас нет стрел')
                        choice = input('Введите номер оружия: ')
                        continue
                print('Вы выбрали {}'.format(temp[int(choice)]))
                print(weapon_list[temp[int(choice)]])
                return weapon_list[temp[int(choice)]]

            else:
                choice = input('Введите номер оружия: ')

    def save_game(self):
        self.game_saved = True
        self.save_hp = self.hp
        self.save_monster_dead = self.monster_dead
        self.save_weapons_list = self.weapons_list
        self.save_summary_arrows = self.summary_arrows

    def load_game(self):
        self.hp = self.save_hp
        self.monster_dead = self.save_monster_dead
        self.weapons_list = self.save_weapons_list
        self.summary_arrows = self.save_summary_arrows



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
                print('Вы заблокировали атаку дальнего боя')
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
                print('Вы заблокировали магическую атаку')
                return 0
            else:
                print('Вы не смогли заблокировать атаку')
                return enemy_attack[0]
        else:
            print('Особая способность неактивная против данного противника')
            return enemy_attack[0]



