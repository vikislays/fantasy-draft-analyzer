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
        
    average = round(total_points/games_played, 1)
    
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
        points = float(row[3]) if row[3] else 0  
        if player_name in player_totals:
            player_totals[player_name] += points
        else:
            player_totals[player_name] = points

    return player_totals        

def main():
    players = load_file()
    while True:
        try:
            print_menu()
            menu_selection = int(input("Enter [1-6] for the menu option you would like to select: "))
            
            if menu_selection == 1:
                player_name = input("Enter player name: ")
                player_name = "Cade Otton"
                find_player(players, player_name)
            elif menu_selection == 2:
                player_totals = sum_player_totals(players)
            elif menu_selection == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError as e:
            print("Invalid input. Enter a number only.")


if __name__ == '__main__':
    main()