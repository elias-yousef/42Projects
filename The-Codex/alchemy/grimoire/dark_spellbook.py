from .dark_validator import dark_validate


def dark_spell_allowed_ingredients() -> list:
    return (["bats", "frogs", "arsenic", "eyeball"])


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if dark_validate(ingredients) == "VALID":
        return ("Spell recorded" +
                f"{spell_name}" + f"({ingredients}" + "- VALID)")
    else:
        return ("rejected")
