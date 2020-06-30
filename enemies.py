from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Abstract class for enemies."""
    damage = random.randint(5, 10)
    hp = random.randint(20, 50)

    @abstractmethod
    def attack(self, damage=damage):
        pass


class Orc(Enemy):
    """Orc melee enemy."""
    damage = Enemy.damage
    hp = Enemy.hp

    def attack(self, damage: int = damage):
        """Melee attack of Orc."""
        print('Орк атаковал вас в ближнем бою')
        return damage, 'melee'


class AngryElf(Enemy):
    """Alien enemy from UFO."""
    damage = Enemy.damage
    hp = Enemy.hp

    def attack(self, damage: int = damage):
        """Range attack of elf."""
        print('Эльф стреляет в вас из лука')
        return damage, 'range'


class Warlock(Enemy):
    """Vampire."""
    damage = Enemy.damage
    hp = Enemy.hp

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
