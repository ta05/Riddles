import numpy as np
import random


def generateBoxes(size):
    boxes = np.linspace(1, size, size, dtype="int").tolist()
    random.shuffle(boxes)
    return boxes


def no_collusion(num_players):
    boxes = generateBoxes(num_players)
    chances = int(num_players/2)
    num_found_key = 0
    for i in range(num_players):
        select = i
        player_boxes = boxes
        random.shuffle(player_boxes)
        player_choices = player_boxes[0:chances]
        # print("Player " + str(i+1) + ": " + " -> ".join([str(choice) for choice in player_choices]) + " ", end="")
        if (select + 1) in player_choices:
            # print("Key Found!", end="")
            num_found_key += 1
        else:
            # print("Key Not Found...", end="")
            pass
        # print()
    return num_found_key == num_players


def box_hopper(num_players):
    boxes = generateBoxes(num_players)
    chances = int(num_players/2)
    num_found_key = 0
    for i in range(num_players):
        # print("Player " + str(i+1) + ": ", end="")
        select = i
        for j in range(chances):
            # print(str(select+1) + ":" + str(boxes[select]) + " -> ", end="")
            if boxes[select] == i + 1:
                # print("Key Found!", end="")
                num_found_key += 1
                break
            else:
                select = boxes[select] - 1
        # print()

    return num_found_key == num_players

def get_strategies():
    return {
        "1": no_collusion,
        "2": box_hopper
    }

def test_games(num_tests, num_players):
    strategies = get_strategies()
    losses = 0
    wins = 0
    selection = input("Please select a strategy:\n" + "\n".join([key + ": " + strategies[key].__name__ for key in strategies]) +"\n\n")
    
    while selection not in strategies.keys():
        selection = input("Please select a valid strategy:\n" + "\n".join([key + ": " + strategies[key].__name__ for key in strategies]) +"\n\n")
    
    for i in range(num_tests):
        if strategies[selection](num_players):
            wins += 1
        else:
            losses += 1
    print("There were {} games. {} wins and {} losses for a {:.2f}% win rate".format(wins + losses, wins, losses, wins / (wins + losses) * 100))


def main():
    test_games(10000, 10)


if __name__ == "__main__":
    main()
