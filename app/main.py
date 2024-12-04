from app.config.knights_config import KNIGHTS
from app.knight_arena.prepare_for_battle import create_knight
from app.knight_arena.fight import Fight
from app.results.result import Result


def battle(knights_config: dict) -> dict:
    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    first_fight = Fight(lancelot, mordred)
    first_fight.start_battle()

    second_fight = Fight(arthur, red_knight)
    second_fight.start_battle()

    result = Result(lancelot, arthur, mordred, red_knight)
    return result.print_result()


battle(KNIGHTS)
