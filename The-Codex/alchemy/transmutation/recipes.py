from alchemy.potions import strength_potion
from ..elements import create_air
from ..potions import creat_fire


def lead_to_gold() -> str:
    return ("Recipe transmuting \
Lead to Gold: brew '" + create_air() + "' and \
'" + strength_potion() + "' mixed\
with '" + creat_fire() + "'")
