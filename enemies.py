from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Abstract class for enemies."""
    damage = random.randint(5, 10)
    hp = random.randint(20, 50)
    @abstractmethod
    def attack(self, damage=damage):
        pass


class Zombie(Enemy):
    """Homeless enemy """
    damage = Enemy.damage
    hp = Enemy.hp
    def attack(self, damage: int = damage):
        """Throwing the shit or garbage."""
        print('Зомби кинул в вас говном')
        return damage


class Alien(Enemy):
    """Alien enemy from UFO."""
    damage = Enemy.damage
    hp = Enemy.hp
    def attack(self, damage: int = damage):
        """using laser"""
        print('Инопланетянин стрельнул в вас лезером')
        return damage


class Vampire(Enemy):
    """Vampire."""
    damage = Enemy.damage
    hp = Enemy.hp
    def attack(self, damage: int = damage):
        print('Вампир чмокнул вас в шею')
        return damage


class EnemyFactory(ABC):
    """AbstractFactory of enemies."""
    @abstractmethod
    def create_enemy(self):
        """Creating an enemie."""
        pass


class ZombieFactory(EnemyFactory):
    """Zombie factory"""
    def create_enemy(self):
        return Zombie()


class AlienFactory(EnemyFactory):
    """Alien factory"""
    def create_enemy(self):
        return Alien()


class VampireFactory(EnemyFactory):
    """Vampire factory"""
    def create_enemy(self):
        return Vampire()


