import csv

players = []

def print_menu():
    print("---Main Menu---")
    print("1 - Print Player Statistics")
    print("0 - Quit")

def load_file():
    with open('nfl_player_stats.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            players.append(row)

def find_player(player_name):
    for row in players:
        if row[0] == player_name:
            print(row)

def main():
    load_file()
    while True:
        try:
            print_menu()
            menu_selection = int(input("Enter [1-6] for the menu option you "
                                        "would like to select: "))
            if menu_selection == 1:
                player_name = input("Enter player name: ")
                find_player(player_name)
            elif menu_selection == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError as e:
            print("Invalid input. Enter a number only.")


if __name__ == '__main__':
    main()