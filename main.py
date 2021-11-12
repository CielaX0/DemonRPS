import random
import var


def game():
    while True:
        counter = random.choice(['Rock', 'Paper', 'Scissors'])
        shoot = input("Shoot, Mortal...")
        shoot = shoot.capitalize()

        if shoot == counter:
            print(random.choice(var.tie))

        if shoot == 'Rock' and counter == 'Scissors' or shoot == 'Scissors' and \
             counter == 'Paper' or shoot == 'Paper' and counter == 'Rock':
            var.last_move = shoot
            var.player_score += 100
            print(str(var.player_score) + " " + str(var.bot_score))
            print(random.choice(var.win))
        elif counter == 'Rock' and shoot == 'Scissors' or counter == 'Scissors' and \
            shoot == 'Paper' or counter == 'Paper' and shoot == 'Rock':
            var.last_move = shoot
            var.bot_score += 100
            print(str(var.player_score) + " " + str(var.bot_score))
            print(random.choice(var.lose))

        if var.player_score == 1000:
            print("I will not be silenced for long...\n")
            return

        elif var.bot_score == 1000:
            print("You belong to me now.\n")
            return


print(game())
