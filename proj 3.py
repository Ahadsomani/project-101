import random

def print_dice(number):
    if number == 1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("---------")
    elif number == 3:
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    elif number == 5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    elif number == 6:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")

response = "y"

while response == "y":
    no = random.randint(1, 6)
    print_dice(no)
    response = input("Roll again? (y/n): ").lower()

print("Goodbye!")
