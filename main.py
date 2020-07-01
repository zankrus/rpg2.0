"""Код домашнего задания."""
from time import sleep, time

import enemies
import Heroes
import Items
import random
from colorama import Fore

print(Fore.GREEN + 'Начало великой RPG-игры "Герой и Чудовища"')
print('Ваша задача убить 10 монстров и не умереть')

while True:
    type_selector = input('Выберите класс вашего героя . 1 - воин  , 2 - лучник , 3 - маг : ')
    if type_selector == '1':
        hero = Heroes.Warrior()
        input_name = input('Введите имя персонажа: ')
        hero.name = input_name
        break
    elif type_selector == '2':
        hero = Heroes.Archer()
        input_name = input('Введите имя персонажа: ')
        hero.name = input_name
        break
    elif type_selector == '3':
        hero = Heroes.Mage()
        input_name = input('Введите имя персонажа: ')
        hero.name = input_name
        break
    else:
        print('Вы ввели неверное значение. Выберите класс')
dead = False
while hero.monster_dead != 10:
    random_event = random.randint(1, 2)
    if random_event == 1:
        '''Битва с монстром'''
        enemy = enemies.spawner()
        while True:
            choice = input('Введите 1, чтобы драться или 2, чтобы убежать : ')
            print('Вы ввели {0}'.format(choice))
            if choice == '1':
                print('Началась драка')
                count = 1
                while True:
                    print('')
                    print('Начался {} раунд боя'.format(count))
                    enemy.hp = enemy.hp - hero.hero_attack()
                    if enemy.hp <= 0:
                        print('У монстра осталось - 0 жизней')
                        print('Монстр побежден')
                        hero.hp = hero.hp - hero.special_class_skill(enemy.attack())
                        hero.monster_dead += 1
                        break
                    print('У монстра осталось - {} жизней'.format(enemy.hp))
                    hero.hp = hero.hp - hero.special_class_skill(enemy.attack())

                    if hero.hp <= 0:
                        print('')
                        print('Вы умерли')
                        dead = True
                        break
                    count += 1
                    print('У вас осталось - {} жизней'.format(hero.hp))
                break
            elif choice == '2':
                print('Вы сбежали')
                break
            else:
                print('Вы ввели неверное значение. Введите 1 или 2')
    elif random_event == 2:
        item = Items.item_spawner()
        if item.name in ('sword', 'bow', 'spell book'):
            print(Fore.BLUE + 'Вы обнаружили {0} с силой - {1}'.format(item.name, item.attack_power))
            hero.take_weapon(item.attack())
            print('Ваш инвентарь - ' +  str(hero.weapons_list))
        elif item.name == 'arrows':
            print('Вы обнаружили стрелы')
            hero.summary_arrows += item.attack()
        elif item.name == 'apple':
            print('ВЫ нашли яблоко')
            hero.hp += item.heal()
            print("Кол-во жизней : " + str(hero.hp))
        elif item.name == 'totem':
            print('Вы нашли ТОТЕМ')
            print('ВЫ можете сохранить игру')
            while True:
                choice = input('Введите 1 ,чтобы сохранится '
                               'или 2, чтобы пройти мимо : ')
                if choice == '1':
                    sleep(1)
                    hero.save_game()
                    print('Игра сохранена. Здоровье {}, Оружие {}'.format(hero.hp, hero.weapons_list))
                    break
                elif choice == '2':
                    print('Вы прошли мимо')
                    break
                else:
                    print('Вы ввели неверное значение. Введите 1 или 2')
    if dead:
        if hero.game_saved == True:
            print('Вы можете загрузится')
            while True:
                choice = input('Введите 1 ,чтобы загрузится '
                               'или 2, чтобы закончить игру : ')
                if choice == '1':
                    sleep(1)
                    hero.load_game()
                    print('Загружена')
                    print('Ваше здоровье {}, ваш инвентарь {}'.format(hero.hp, hero.weapons_list))
                    break
                elif choice == '2':
                    print('Вы проиграли')
                    break
                else:
                    print('Вы ввели неверное значение. Введите 1 или 2')
        else:
            print('Вы проиграли')
            quit()
    print('Монстров убито {}'.format(hero.monster_dead))
    sleep(1)
