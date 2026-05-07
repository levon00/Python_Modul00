def helper_func(a: int) -> None:
    if a > 0:
        helper_func(a - 1)
    print(f"Day {a}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    helper_func(days)
    print("Harvest time!")
