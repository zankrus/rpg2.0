from abc import ABC, abstractmethod
import random


class Item(ABC):
    """Abtsracrt items class"""
    name = ''
    def get_item(self):
        """Take item"""
        return self


class Sword(Item):
    """Sword"""
    attack_power = random.randint(1, 20)
    name = 'sword'
    def attack(self, attack_power: int = attack_power):
        return 'sword', attack_power


class Bow(Item):
    """Sword"""
    attack_power = random.randint(1, 20)
    name = 'bow'
    def attack(self, attack_power: int = attack_power):
        return 'Bow', attack_power


class Arrows(Item):
    """Sword"""
    arrows = random.randint(1, 20)
    name = 'arrows'
    attack_power = 0
    def attack(self, additional_arrows: int = arrows):
        return additional_arrows


class SpellBook(Item):
    """Spell Book"""
    attack_power = random.randint(1, 20)
    name = 'spell book'
    def attack(self, attack_power: int = attack_power):
        return "Spell book", attack_power


class Apple(Item):
    """Healing apple"""
    name = 'apple'
    attack_power = 0
    def heal(self):
        return random.randint(1, 20)


class Totem(Item):
    """Totem"""
    name = 'totem'
    attack_power = 0


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


class ArrowsFactory(ItemFactory):
    """Abstract class for items"""

    def spawn_item(self):
        return Arrows()

def item_spawner():
    spawner_to_factory_mapping = {
        "sword": SwordFactory,
        "bow":BowFactory,
        "apple": AppleFactory,
        "spellbook":SpellBookFactory,
        "totem": TotemFactory,
        "arrow": ArrowsFactory
    }
    item_type_list = ["sword", "bow", "apple",  "spellbook","totem","arrow"]
    SPAWNER_TYPE = random.choice( item_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    item = spawner.spawn_item()
    return item