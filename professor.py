import random

def main():
    level = get_level()
    correct = 0
    incorrect = 0
    incorrect_problems = []
    for i in range(10):
        x, y = generate_integer(level)
        while True:
            answer = input(f"{x} + {y} = ")
            if not answer.isdigit():
                print("EEE")
                incorrect += 1
                incorrect_problems.append(f"{x} + {y} = {x + y}")
                if incorrect == 3:
                    print("The correct answer is:", f"{x} + {y} = {x+y}")
                    break
            else:
                try:
                    if int(answer) == x + y:
                        correct += 1
                        break
                    else:
                        print("EEE")
                        incorrect += 1
                        incorrect_problems.append(f"{x} + {y} = {x + y}")
                        if incorrect == 3:
                            print(f"{x} + {y} = {x+y}")
                            break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        if incorrect == 3:
            continue
    print(f"Score: {correct}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ('1', '2', '3'):
            return int(level)


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
