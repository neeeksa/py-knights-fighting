from app.config.knights_config import KNIGHTS
from app.knight_arena.prepare_for_battle import battle_preparations
from app.peoples.knight_create import KnightCreate
from app.knight_arena.fight import Fight
from app.results.result import Result


def battle(knights_config: dict) -> dict:
    lancelot = KnightCreate(knights_config["lancelot"])
    battle_preparations(lancelot)

    arthur = KnightCreate(knights_config["arthur"])
    battle_preparations(arthur)

    mordred = KnightCreate(knights_config["mordred"])
    battle_preparations(mordred)

    red_knight = KnightCreate(knights_config["red_knight"])
    battle_preparations(red_knight)

    first_fight = Fight(lancelot, mordred)
    first_fight.start_battle()

    second_fight = Fight(arthur, red_knight)
    second_fight.start_battle()

    result = Result(lancelot, arthur, mordred, red_knight)
    return result.print_result()


battle(KNIGHTS)
