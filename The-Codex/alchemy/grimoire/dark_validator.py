from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate(ingredients: str) -> str:
    allow_list = dark_spell_allowed_ingredients()
    lower_case = ingredients.lower()
    for item in allow_list:
        if item in lower_case:
            return ("VALID")
        else:
            return ("INVALID")
    return ("will not happen")
