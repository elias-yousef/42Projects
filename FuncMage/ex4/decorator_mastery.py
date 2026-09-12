from collections.abc import Callable
from functools import wraps
import time
import random
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def count_speed(*args: Any, **Kwargs: Any) -> Any:
        start = time.perf_counter()
        print(f"casting {func.__name__}...")
        result = func(*args, **Kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return (result)
    return (count_speed)


def power_validator(min_power: int) -> Callable[..., Any]:
    def decerator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def Wrapper(*args: Any, **Kwargs: Any) -> Any:
            pow: Any = Kwargs.get("power")
            if not pow:
                for arg in args:
                    if isinstance(arg, int):
                        pow = arg
                        break
            if pow < min_power:
                return "Insufficient power for this spell"
            return func(*args, **Kwargs)
        return Wrapper
    return decerator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decerator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def Wrapper(*args: Any, **Kwargs: Any) -> Any:
            attempts = 1
            while attempts <= max_attempts:
                try:
                    return (func(*args, **Kwargs))
                except Exception:
                    if attempts < max_attempts:
                        print(f"Spell failed, \
retrying... (attempt {attempts}/{max_attempts})")
                    elif attempts == max_attempts:
                        print(f"Spell casting failed after \
{max_attempts} attempts")
                        print("Waaaaaaagh spelled !")
                attempts += 1
        return Wrapper
    return decerator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        checker = True
        if len(name) < 3:
            return False
        for letter in name:
            if letter.isalpha() or letter.isspace():
                pass
            else:
                checker = False
        return checker

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    test_powers = [29, 18, 30, 12]
    spell_names = ['tornado', 'meteor', 'shield', 'fireball']
    mage_names = ['Phoenix', 'Storm', 'Kai']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:

        return "Result: Fireball cast!"
    print(fireball())

    print("\nTesting retrying spell...")

    @power_validator(min_power=20)
    def power_val(power: int) -> str:
        return f"power: {power} plus 3 = {power + 3}"

    for i in range(len(test_powers)):
        print(power_val(test_powers[i]))
    print("\nTesting retrying spell...")

    @retry_spell(5)
    def generator() -> None:
        if random.random() < 0.8:
            raise Exception("Engine sputtered out!")
        print("VROOM! Engine is running.")
    generator()
    print("\nTesting MageGuild...")

    Mage = MageGuild()
    for i in range(len(mage_names)):
        print(Mage.validate_mage_name(mage_names[i]))
    for i in range(len(invalid_names)):
        print(Mage.validate_mage_name(invalid_names[i]))

    print(Mage.cast_spell(spell_name="Lightning", power=15))
    print(Mage.cast_spell("unknown spill", 9))
