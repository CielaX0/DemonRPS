import random


def game():
    player_score = None
    bot_score = None

    while True:
        counter = random.choice(['Rock', 'Paper', 'Scissors'])
        shoot = input("Shoot, Mortal...")
        shoot = shoot.capitalize()

        if shoot == counter:
            print(random.choice(["A draw. We're not finished yet.\n", "Tie Game.\n", "....again.\n"]))

        if shoot == 'Rock' and counter == 'Scissors' or shoot == 'Scissors' and counter == 'Paper' or shoot == 'Paper' and \
                counter == 'Rock':
            player_score += 100
            print(str(player_score) + " " + str(bot_score))
            print(random.choice(["The Gods seem to favor you.\n", "...", "Your skill is...respectable.\n"]))
        elif counter == 'Rock' and shoot == 'Scissors' or counter == 'Scissors' and shoot == 'Paper' or counter == 'Paper' and \
                shoot == 'Rock':
            bot_score += 100
            print(str(player_score) + " " + str(bot_score))
            print(random.choice(["As expected.\n", "A loss...for you.\n", "Typical Mortal strategy.\n", "Good.\n"]))

        if player_score == 1000:
            print("I will not be silenced for long...\n")
            return
        elif bot_score == 1000:
            print("You belong to me now.\n")
            return


print(game())
