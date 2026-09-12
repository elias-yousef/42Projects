from collections.abc import Callable
import operator
from typing import Any
from functools import partial, reduce, singledispatch, lru_cache


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanted {target} with {power} {element} power!"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        x = reduce(operator.add, spells)
    elif operation == "multiply":
        x = reduce(operator.mul, spells)
    elif operation == "max":
        x = reduce(max, spells)
    elif operation == "min":
        x = reduce(min, spells)
    else:
        raise ValueError("operation is unknown, try again\n")
    return x


def partial_enchanter(
        base_enchantment: Callable[..., Any]
        ) -> dict[str, Callable[..., Any]]:
    fire_spell = partial(base_enchantment, power=50, element="fire")
    ice_spell = partial(base_enchantment, power=50, element="Ice")
    lightning_spell = partial(base_enchantment, power=50, element="Lightning")
    return {
        "fire": fire_spell,
        "ice": ice_spell,
        "lightning": lightning_spell
        }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def process_spell(data: Any) -> str:
        return "Unknown spell type"

    @process_spell.register(int)
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @process_spell.register(str)
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @process_spell.register(list)
    def _(data: list[Any]) -> str:
        return f"Multi-cast: {len(data)} spells"

    return process_spell


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    operations = ["add", "multiply", "max", "min"]
    try:
        added_number = spell_reducer(numbers, "add")
        mul_numbers = spell_reducer(numbers, "multiply")
        max_number = spell_reducer(numbers, "max")
        print(f"sum: {added_number}")
        print(f"Product: {mul_numbers}")
        print(f"max: {max_number}")
    except ValueError as error:
        print(error)
    print("\nTesting partial enchanter...")
    i = partial_enchanter(base_enchantment)
    print(i["fire"](target="Shield"))
    print(i["ice"](target="Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    testing = spell_dispatcher()
    print(testing(10))
    print(testing("fireball"))
    print(testing(["spell1", "spell2", "spell3"]))
    print(testing(14.5))
