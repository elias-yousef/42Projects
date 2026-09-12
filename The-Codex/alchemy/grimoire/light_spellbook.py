def light_spell_allowed_ingredients() -> list:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    if "VALID" in validate_ingredients(ingredients):
        return ("Spell recorded" + f" {spell_name}"
                + f"({ingredients}" + " - VALID)")
    else:
        return ("rejected")
