import csv
from decimal import Decimal, ROUND_HALF_UP

def print_menu():
    print("===============================")
    print("Main Menu")
    print("===============================")
    print("1 - Print Player Card")
    print("2 - Top Ten Players by Points")
    print("3 - Quit")
    print("\n")


def load_file():
    players = []
    with open('nfl_player_stats.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            players.append(row)
    return players


def print_player_card(player_name, players):
    position = ""
    games = list()
    for row in players:
        if row[0] == player_name:       
            position = row[1]
            games.append((row[2], row[3]))

    print("\n")
    print("===============================")
    print(f"{player_name}, {position}")
    print("===============================")
    total_points = 0
    games_played = 0
    for game in games:
        points = game[1]
        if points:
            total_points += round_number(points)
            games_played += 1
            print(f"GW {game[0]}: \t {points} pts")
        else:
            print(f"GW {game[0]}: \t BYE")
    
    if games_played > 0:
        average = round(total_points/games_played, 1)
    else:
        average = 0
    
    print("===============================")
    print(f"Total points: {total_points}")
    print(f"Games played: {games_played}")
    print(f"Points per game: {average}")
    print("\n")


def find_player(players, player_name):
    matched_players = []
    for row in players:
        if player_name.lower() in row[0].lower():
            if row[0] not in matched_players: 
                matched_players.append(row[0])
    return matched_players    


def round_number(point):
    value = Decimal(point)
    rounded = value.quantize(Decimal("0.0"), rounding=ROUND_HALF_UP)
    return rounded


def sum_player_totals(players):
    player_totals = {}
    for row in players:
        player_name = row[0]
        position = row[1]
        points = row[3] if row[3] else 0
        points = round_number(points)
        if player_name in player_totals:
            player_totals[player_name][0] += points 
        else:
            player_totals[player_name] = [points, position]

    return player_totals


def get_top_players(player_totals, player_position, number_of_ranked_players):
    totals_list = []
    for name in player_totals:
        points = player_totals[name][0]
        position = player_totals[name][1]

        if position == player_position or player_position == "ALL":
            totals_list.append([name, points, position])

    for i in range(len(totals_list)):
        for j in range(i + 1, len(totals_list)):
            if totals_list[j][1] > totals_list[i][1]:
                totals_list[i], totals_list[j] = totals_list[j], totals_list[i]

    return totals_list[0:number_of_ranked_players]


def get_longest_name_length(players):
    maximum_length = 0
    for row in players:
        player = row[0]
        if len(player) > maximum_length:
            maximum_length = len(player)

    return maximum_length

def main():
    players = load_file()
    player_totals = sum_player_totals(players)

    while True:
        try:
            print_menu()
            menu_selection = int(input("Enter [1-3] for the menu option you would like to select: "))
            
            if menu_selection == 1:
                player_name = input("Enter player name: ")
                matched_players = find_player(players, player_name)
                if len(matched_players) == 0:
                    print("No players found.")
                elif len(matched_players) == 1:
                    print_player_card(matched_players[0], players)  
                else:
                    print("Matched multiple players.")
                    for i in range(0, len(matched_players)):
                        print(f"{i + 1}. {matched_players[i]}")
                    try:
                        player_index = int(input("Choose which one you want by entering number next to name: "))
                        if player_index in range(1, len(matched_players) + 1):
                            print_player_card(matched_players[player_index - 1], players)
                        else:
                            print("Invalid input.")    
                    except ValueError:
                        print("Invalid input.")

            elif menu_selection == 2:
                player_position = input("Please choose position (WR, RB, TE, ALL(default)): ")
                player_position = player_position.upper()

                if len(player_position.strip()) == 0:
                    player_position = "ALL"
                
                if player_position not in ("WR", "RB", "TE", "ALL"):
                    print("Invalid input. Try one of the options.")
                    continue
                
                total_number_of_players = len(player_totals)
                try:
                    number_of_ranked_players = int(input(f"Please choose how many players you'd like to compare (1-{total_number_of_players}): "))
                    if number_of_ranked_players not in range(1, total_number_of_players + 1):
                        print(f"Invalid Selection. Choose number between 1 and {total_number_of_players}. Default: 10")
                        continue    
                except ValueError:
                    number_of_ranked_players = 10

                top_players = get_top_players(player_totals, player_position, number_of_ranked_players)

                longest = get_longest_name_length(top_players)

                if len(top_players) < number_of_ranked_players:
                    number_of_ranked_players = len(top_players)
                
                print("\n")
                print("===============================")
                print(f"Top {number_of_ranked_players} Players by Points")
                print("===============================")
                    
                for i in range(number_of_ranked_players):
                    name = top_players[i][0]
                    padding_needed = longest - len(name)
                    padded_name = name
                    for pad in range(padding_needed):
                        padded_name += " "

                    points = top_players[i][1]
                    position = top_players[i][2]
                    print(f"{i + 1}. \t{padded_name} ({position}): {points} pts")
                print("\n")
            elif menu_selection == 3:
                break
            else:
                print("Invalid selection.")
        except ValueError as e:
            print("Invalid input. Enter a number only.")


if __name__ == '__main__':
    main()