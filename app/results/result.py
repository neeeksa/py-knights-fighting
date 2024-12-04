from app.peoples.knight_create import KnightCreate


class Result:
    def __init__(self, first_knight: "KnightCreate",
                 second_knight: "KnightCreate",
                 third_knight: "KnightCreate",
                 fourth_knight: "KnightCreate") -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight
        self.third_knight = third_knight
        self.fourth_knight = fourth_knight

    def print_result(self) -> dict:
        return {
            self.first_knight.name: self.first_knight.hp,
            self.second_knight.name: self.second_knight.hp,
            self.third_knight.name: self.third_knight.hp,
            self.fourth_knight.name: self.fourth_knight.hp
        }
