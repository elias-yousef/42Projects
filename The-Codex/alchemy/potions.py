from .elements import create_earth
from elements import creat_water
from .elements import create_air
from elements import creat_fire


def healing_potion() -> str:
    return "Healing potion \
brewed with " + create_earth() + " and " + create_air()


def strength_potion() -> str:
    return "Strength \
potion brewed \
with " + creat_fire() + " and " + creat_water()
