from abc import ABC, abstractmethod
from ex0.CreatureFactory import Creature, CreatureFactory


class HealCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def heal(self, target: str = "small") -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self, target: str = "small") -> str:
        return (f"Sproutling heals itself for a {target} amount")

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self, target: str = "small") -> str:
        return (f"Bloomelle heals itself and others for a {target} amount")

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance!")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed = False

    def transform(self) -> str:
        self.is_transformed = True
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        self.is_transformed = False
        return ("Shiftling returns to normal.")

    def attack(self) -> str:
        if self.is_transformed:
            return ("Shiftling performs a boosted strike!")
        else:
            return ("Shiftling attacks normally.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed = False

    def transform(self) -> str:
        self.is_transformed = True
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.is_transformed = False
        return ("Morphagon stabilizes its form.")

    def attack(self) -> str:
        if self.is_transformed:
            return ("Morphagon unleashes a devastating morph strike!")
        else:
            return ("Morphagon attacks normally.")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
