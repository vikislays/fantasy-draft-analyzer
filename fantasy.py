def print_menu():
    print("---Main Menu---")
    print("1 - Print Player Statistics")
    print("0 - Quit")



def main():
    while True:
        try:
            print_menu()
            menu_selection = int(input("Enter [1-6] for the menu option you "
                                        "would like to select: "))
            if menu_selection == 1:
                pass
            elif menu_selection == 0:
                break
            else:
                print("Invalid selection.")
        except ValueError as e:
            print("Invalid input. Enter a number only.")


if __name__ == '__main__':
    main()