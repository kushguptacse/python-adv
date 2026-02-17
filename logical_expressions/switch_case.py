def guessing_game(val: int) -> None:
    match val:
        case val if val < 0:  # val negative
            print(f"{val} is <0")
        case val if val % 2 == 0:
            print(f"{val} is even")
        case 1 | 3 | 5:
            print(f"{val} is 1,3,5")
        case 101:
            print(f"{val}")
        case _:
            print(f"default case: {val}")


guessing_game(-1)
guessing_game(46)
guessing_game(3)
guessing_game(101)
guessing_game(7) # default case

