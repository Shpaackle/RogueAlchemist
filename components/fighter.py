from typing import List

from game_messages import Message


class Fighter:
    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount: int)->List[dict]:
        results: List[dict] = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({"dead": self.owner})

        return results

    def attack(self, target)->List[dict]:
        results: List[dict] = []

        damage: int = self.power - target.fighter.defense

        if damage > 0:
            results.append({"message": Message(f"{self.owner.name.capitalize()} attacks {target.name} for {str(damage)} hit points.", "white")})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({"message": Message(f"{self.owner.name.capitalize()} attacks {target.name} but does no damage.", "white")})

        return results
