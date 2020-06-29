from abc import ABC, abstractmethod
import random


class Item(ABC):
    """Abtsracrt items class"""

    def get_item(self):
        """Take item"""
        return self


class Sword(Item):
    """Sword"""
    attack_power = random.randint(1, 20)

    def attack(self, attack_power: int = attack_power):
        return 'sword', attack_power


class Bow(Item):
    """Sword"""
    attack_power = random.randint(1, 20)

    def attack(self, attack_power: int = attack_power):
        return 'Bow', attack_power


class SpellBook(Item):
    """Spell Book"""
    attack_power = random.randint(1, 20)

    def attack(self, attack_power: int = attack_power):
        return "Spell book", attack_power


class Apple(Item):
    """Healing apple"""
    def heal(self):
        return random.randint(1, 20)


class Totem(Item):
    """Totem"""
    def save_game(self):
        pass

class ItemFactory(ABC):
    """Abstract class for items"""
    def spawn_item(self):
        pass


class SwordFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return Sword()


class BowFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return Bow()


class SpellBookFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return SpellBook()


class AppleFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return Apple()

class TotemFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return Totem()

