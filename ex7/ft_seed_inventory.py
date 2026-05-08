def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    word = seed_type.capitalize()
    if unit == "packets":
        print(f"{word} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{word} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{word} seeds: {unit} {quantity} square meters")
    else:
        print("Unknown unit type")
