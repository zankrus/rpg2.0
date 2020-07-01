from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Abstract class for enemies."""
    damage = random.randint(5, 10)
    hp = random.randint(20, 50)
    enemy_type = ''
    @abstractmethod
    def attack(self, damage=damage):
        pass


class Orc(Enemy):
    """Orc melee enemy."""
    damage = Enemy.damage
    hp = Enemy.hp
    enemy_type = 'ORC'

    def attack(self, damage: int = damage):
        """Melee attack of Orc."""
        print('Орк атаковал вас в ближнем бою')
        return damage, 'melee'


class AngryElf(Enemy):
    """Alien enemy from UFO."""
    damage = Enemy.damage
    hp = Enemy.hp
    enemy_type = 'ELF'

    def attack(self, damage: int = damage):
        """Range attack of elf."""
        print('Эльф стреляет в вас из лука')
        return damage, 'range'


class Warlock(Enemy):
    """Vampire."""
    damage = Enemy.damage
    hp = Enemy.hp
    enemy_type = 'WARLOCK'

    def attack(self, damage: int = damage):
        print('Злой маг пульнул в вас фаербол')
        return damage, 'spell'


class EnemyFactory(ABC):
    """AbstractFactory of enemies."""

    @abstractmethod
    def create_enemy(self):
        """Creating an enemie."""
        pass


class OrcFactory(EnemyFactory):
    """Zombie factory"""

    def create_enemy(self):
        return Orc()


class AngryElfFactory(EnemyFactory):
    """Alien factory"""

    def create_enemy(self):
        return AngryElf()


class WarlockFactory(EnemyFactory):
    """Vampire factory"""

    def create_enemy(self):
        return Warlock()

def spawner():
    spawner_to_factory_mapping = {
        "orc": OrcFactory,
        "angryelf":AngryElfFactory,
        "warlock": WarlockFactory}
    enemy_type_list = ["orc", "angryelf", "warlock"]
    SPAWNER_TYPE = random.choice(enemy_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    enemy = spawner.create_enemy()
    print('Вы встретили врага {0}, с жизнями {1} и атакой {2}'.format(enemy.enemy_type, enemy.hp, enemy.damage))
    return enemy