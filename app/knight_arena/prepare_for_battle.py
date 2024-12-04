from app.peoples.knight_create import KnightCreate


def battle_preparations(knight: "KnightCreate") -> None:
    knight.apply_protection()
    knight.apply_power()
    knight.apply_potion()


def create_knight(knight_config: dict) -> KnightCreate:
    knight = KnightCreate(knight_config)
    battle_preparations(knight)
    return knight
