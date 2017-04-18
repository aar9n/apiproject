from swfunc import *

peopleurl = "http://swapi.co/api/people"
filmurl = "http://swapi.co/api/films"

# people = getAllPages(peopleurl)
films = getAllPages(filmurl)
print('Films:')
printItems(films, "title")
done = False
while not done:
    choice = input('Enter the number of the film you would like to explore: ')
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

    choice = input("Would you like to explore the characters (C), planets (P), vehicles (V), or starships (S) of %s? Select one: " % (film["title"]))

    if choice.lower() == 'c':
        urls = (film["characters"])
        getItemList(urls)

    elif choice.lower() == 'p':
        urls = (film["planets"])
        getItemList(urls)

    elif choice.lower() == 'v':
        urls = (film["vehicles"])
        getItemList(urls)

    elif choice.lower() == 's':
        urls = (film["starships"])
        getItemList(urls)

    elif choice.lower() == 'q':
        done = True

    else:
        print('Invalid entry. Try again!')
        continue
