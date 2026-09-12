from abc import ABC, abstractmethod
from ex0.CreatureFactory import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class BattleStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def act(self, fighter: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, fighter: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, fighter: Creature) -> bool:
        return True

    def act(self, fighter: Creature) -> None:
        if not self.is_valid(fighter):
            raise Exception(f"Invalid Creature \
'{fighter.name}' for this strategy")
        else:
            print(fighter.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, fighter: Creature) -> bool:
        if isinstance(fighter, TransformCapability):
            return True
        else:
            return False

    def act(self, fighter: Creature) -> None:
        if not self.is_valid(fighter):
            raise Exception(f"Invalid Creature \
'{fighter.name}' for this strategy")
        else:
            t_fighter = cast(TransformCapability, fighter)
            print(t_fighter.transform())
            print(fighter.attack())
            print(t_fighter.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, fighter: Creature) -> bool:
        if isinstance(fighter, HealCapability):
            return True
        else:
            return False

    def act(self, fighter: Creature) -> None:
        if not self.is_valid(fighter):
            raise Exception(f"Invalid Creature \
'{fighter.name}' for this strategy")
        else:
            t_fighter = cast(HealCapability, fighter)
            print(fighter.attack())
            print(t_fighter.heal())
