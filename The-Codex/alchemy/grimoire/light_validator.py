def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allow_list = light_spell_allowed_ingredients()
    lower_case = ingredients.lower()
    for item in allow_list:
        if item in lower_case:
            return ("VALID")
        else:
            return ("INVALID")
    return ("will not happen")
