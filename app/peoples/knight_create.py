class KnightCreate:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.protection = 0
        self.weapon = config["weapon"]
        self.potion = config["potion"]

    def apply_protection(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

    def apply_power(self) -> None:
        if self.weapon:
            self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]
                self.hp = max(self.hp, 0)
