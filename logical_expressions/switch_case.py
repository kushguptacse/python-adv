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


print("************************")

def handle_data(data):
    match data:
        # guard condition
        case v if isinstance(v, int) and v < 0:
            print("Negative int:", v)
        # exact value
        case 100:
            print("Value is 100")
        # list destructuring
        case [a, b]:
            print("List:", a, b)
        # list variable unpack
        case [first, *mid, last]:
            print("Long list:", first, mid, last)
        # dict destructuring
        case {"name": name, "age": age}:
            print("User:", name, age)
        # default
        case _:
            print("Default:", data)


handle_data(-1) #Negative int: -1
handle_data(100) #Value is 100
handle_data([1, 2]) #List: 1 2
handle_data([1, 2,3,4,5,6]) #Long list: 1 [2, 3, 4, 5] 6
handle_data({"name": "Kush", "age": 25})# User: Kush 25
handle_data("kush") #Default: kush
