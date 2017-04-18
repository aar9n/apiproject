from swfunc import *

peopleurl = "http://swapi.co/api/people"
filmurl = "http://swapi.co/api/films"

# people = getAllPages(peopleurl)
films = getAllPages(filmurl)
print('Films:')
printItems(films, "title")
done = False
while not done:
    choice = input('\n==> Enter the number of the film you would like to explore: ')
    validStrs = [str(x) for x in range(1, len(films) + 1)]

    if choice in validStrs:
        film = films[int(choice) - 1]
        print(film["title"])

    elif choice.lower() == 'q':
        done = True
        continue

    else:
        print('Invalid entry.' +  'Try again!')
        continue

    choice = input("\n==> Would you like to explore the characters (C), planets (P), vehicles (V), starships (S), or attributes (A) of %s? Select one: " % (film["title"]))
    print('')

    if choice.lower() == 'c':
        urls = film["characters"]
        promptForItem(urls, "character")

    elif choice.lower() == 'p':
        urls = (film["planets"])
        promptForItem(urls, "planet")

    elif choice.lower() == 'v':
        urls = (film["vehicles"])
        promptForItem(urls, "vehicle")

    elif choice.lower() == 's':
        urls = (film["starships"])
        promptForItem(urls, "starship")

    elif choice.lower() == 'a':
        printAttributes(film)

    elif choice.lower() == 'q':
        done = True

    else:
        print('Invalid entry. Try again!')
        continue
