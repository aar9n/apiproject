from swfunc import *

def main():
    """
    Main is the central function for prompting the user in my swapi.co explorer.
    run this file in the terminal to use this api explorer! Main includes the
    two outermost while loops of the explorer and the central menu, prompting
    the user to explore either the characters, planets, vehicles, starships,
    or attributes of any given film.
    """
    filmurl = "http://swapi.co/api/films"
    films = getAllPages(filmurl)
    done = False
    while not done:
        print('\nFilms:')
        printItems(films, "title")
        choice = input('\n==> Enter the number of the film you would like to explore: ')
        try:
            if choice.lower() == 'q':
                done = True
                continue
            else:
                film = films[int(choice) - 1]
        except:
            print('Invalid entry: ' + choice + '. Try again!')
            continue

        while not done:
            print('Current film: ' + film["title"])
            choice = input("\n==> Enter (C)haracters, (P)lanets, (V)ehicles, (S)tarships, (A)ttributes, (B)ack, or (Q)uit: ")
            print('')

            if choice.lower() == 'c':
                urls = film["characters"]
                print('Characters: ')
                chars = getItemList(urls, "name")
                promptForItem(chars, "character")

            elif choice.lower() == 'p':
                urls = film["planets"]
                print('Planets: ')
                planets = getItemList(urls, "name")
                promptForItem(planets, "planet")

            elif choice.lower() == 'v':
                urls = film["vehicles"]
                print('Vehicles: ')
                vehicles = getItemList(urls, "name")
                promptForItem(vehicles, "vehicle")

            elif choice.lower() == 's':
                urls = film["starships"]
                print('Starships: ')
                starships = getItemList(urls, "name")
                promptForItem(starships, "starship")

            elif choice.lower() == 'a':
                printAttributes(film)
                print('')

            elif choice.lower() == 'b':
                break

            elif choice.lower() == 'q':
                done = True

            else:
                print('Invalid entry. Try again!')
                continue

main()
