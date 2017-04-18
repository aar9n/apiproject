import requests
import json

def getAllPages(url):
    done = False
    results = []
    while not done:
        # print("Requesting %s" % (url))
        r = requests.get(url)
        page = json.loads(r.content)
        items = page["results"]
        # print("Retrieved %d items" % (len(items)))
        results += items
        if page["next"]:
            url = page["next"]
        else:
            done = True
    return results

def getItem(url):
    r = requests.get(url)
    item = json.loads(r.content)
    return item

def printItems(lst, key):
    idx = 1
    for item in lst:
        print("%d. %s" % (idx, item[key]))
        idx = idx + 1

def getItemList(urls, name):
    itemList = []
    for url in urls:
        item = getItem(url)
        itemList.append(item)
    printItems(itemList, name)
    return itemList

def printAttributes(item):
    for key in item:
        value = str(item[key])
        if key == 'opening_crawl':
            value = "\n" + value + "\n"
        if type(item[key]) is not list:
            print("%s: %s" % (key.title(), value))

def promptForItem(items, swType):
    done = False
    while not done:
        itemChoice = input("\n==> Enter the number of a %s to explore, or select B to go back: " % swType)
        print('')
        try:
            if itemChoice.lower() == 'b':
                done = True
            else:
                item = items[int(itemChoice) - 1]
                printAttributes(item)
        except:
            print('Invalid entry: ' + itemChoice + '. Try again!')


# def goBack()

# def compare(item1, item2):
#     if item1["episode_id"] > item2["episode_id"]:
#         return 1
#     elif item1["episode_id"] < item2["episode_id"]:
#         return -1
#     else:
#         return 0
#
# def sortFilms(films):
#     for film in films:
#         compare(film, )
