import csv

def print_menu():
    print("---Main Menu---")
    print("1 - Print Player Statistics")
    print("2 - Top Ten Players by Points")
    print("0 - Quit")

def load_file():
    players = []
    with open('nfl_player_stats.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            players.append(row)
    return players

def print_player_card(player_name, position, games):
    print("===============================")
    print(f"{player_name}, {position}")
    print("===============================")
    total_points = 0
    games_played = 0
    for game in games:
        points = game[1]
        if points:
            total_points += float(points)
            games_played += 1
            print(f"GW {game[0]}: {points} pts")
        else:
            print(f"GW {game[0]}: BYE")
    if games_played > 0:
        average = round(total_points/games_played, 1)
    else:
        average = 0
    
    print("===============================")
    print(f"Total points: {total_points}")
    print(f"Games played: {games_played}")
    print(f"Points per game: {average}")

def find_player(players, player_name):
    games = list()
    for row in players:
        if row[0] == player_name:
            position = row[1]
            games.append((row[2], row[3]))

    print_player_card(player_name, position, games)

def sum_player_totals(players):
    player_totals = {}
    for row in players:
        player_name = row[0]
        position = row[1]
        points = float(row[3]) if row[3] else 0
        if player_name in player_totals:
            player_totals[player_name][0] += points
        else:
            player_totals[player_name] = [points, position]

    return player_totals


def main():
    players = load_file()
    player_totals = sum_player_totals(players)

    while True:
        try:
            print_menu()
            menu_selection = int(input("Enter [1-6] for the menu option you would like to select: "))
            
            if menu_selection == 1:
                player_name = input("Enter player name: ")
                #player_name = "Cade Otton"
                find_player(players, player_name)
            elif menu_selection == 2:
                player_position = input("Please choose position (WR, RB, TE, ALL(default)): ")
                player_position = player_position.upper()

                if len(player_position.strip()) == 0:
                    player_position = "ALL"
                
                if player_position not in ("WR", "RB", "TE", "ALL"):
                    print("Invalid input. Try one of the options.")
                
                total_number_of_players = len(player_totals)
                number_of_ranked_players = 10  # default
                try:
                    number_of_ranked_players = int(input(f"Please choose how many players you'd like to compare (1-{total_number_of_players}): "))
                    #print(f"total number of ranked players:{number_of_ranked_players}, total number of players:{total_number_of_players}")
                    if number_of_ranked_players not in range(1, total_number_of_players):
                        print(f"Invalid Selection. Choose number between 1 and {total_number_of_players}.")
                        continue    
                except ValueError:
                    print("Invalid Selection.")
                    continue
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

                print("===Top Ten Players by Points===")
                for i in range(number_of_ranked_players):
                    name = totals_list[i][0]
                    points = totals_list[i][1]
                    position = totals_list[i][2]
                    print(f"{i + 1}. {name} ({position}): {points} pts")

                
            elif menu_selection == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError as e:
            print("Invalid input. Enter a number only.")


if __name__ == '__main__':
    main()