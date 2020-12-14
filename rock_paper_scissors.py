import random

def play():
    human = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])

    if human == computer:
        return "It's a tie."

    if is_win(human, computer):
        return "You won!"

    return "You lost!"

def is_win(human, computer):
    if (human == "r" and computer == "s") or (human == "s" and computer == "p") \
        or (human == "p" and computer == "r"):
        return True

print(play())
