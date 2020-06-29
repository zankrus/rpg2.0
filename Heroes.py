from abc import ABC, abstractmethod
import random
import Items

class Hero(ABC):
    """Abstract hero class"""
    hp = 30
    weapons_list = []

    def take_weapon(self, weapon):
        self.weapons_list = {weapon}

    def heal(self, healing_points: int):
        self.hp = self.hp + healing_points
