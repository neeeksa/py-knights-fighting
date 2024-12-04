from typing import Any

from app.peoples.knight_create import KnightCreate


class Fight:
    def __init__(self, first_knight: "KnightCreate",
                 second_knight: "KnightCreate") -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def start_battle(self) -> tuple[Any, Any]:
        damage_to_first_knight = (
            max(self.second_knight.power - self.first_knight.protection, 0))
        self.first_knight.hp -= damage_to_first_knight
        self.fell_checkout()

        damage_to_second_knight = (
            max(self.first_knight.power - self.second_knight.protection, 0))
        self.second_knight.hp -= damage_to_second_knight
        self.fell_checkout()
        return self.first_knight.hp, self.second_knight.hp

    def fell_checkout(self) -> None:
        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0
        if self.second_knight.hp <= 0:
            self.second_knight.hp = 0
