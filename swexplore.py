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
    if choice.lower() == 'c':
        urls = film["characters"]
        chars = getItemList(urls, "name")
        charChoice = input("\n==> Which character would you like to explore? Select a valid number: ")
        char = chars[int(charChoice) - 1]
        printAttributes(char)

    elif choice.lower() == 'p':
        urls = (film["planets"])
        planets = getItemList(urls, "name")
        planetChoice = input("\n==> Which planet would you like to explore? Select a valid number: ")
        planet = planets[int(planetChoice) - 1]
        printAttributes(planet)

    elif choice.lower() == 'v':
        urls = (film["vehicles"])
        vehicles = getItemList(urls, "name")
        vehicleChoice = input("\n==> Which vehicle would you like to explore? Select a valid number: ")
        vehicle = vehicles[int(vehicleChoice) - 1]
        printAttributes(vehicle)

    elif choice.lower() == 's':
        urls = (film["starships"])
        starships = getItemList(urls, "name")
        starshipChoice = input("\n==> Which starship would you like to explore? Select a valid number: ")
        starship = planets[int(starshipChoice) - 1]
        printAttributes(starship)

    elif choice.lower() == 'a':
        printAttributes(film)

    elif choice.lower() == 'q':
        done = True

    else:
        print('Invalid entry. Try again!')
        continue
