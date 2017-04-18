import requests
import json

def getAllPages(url):
    done = False
    results = []
    while not done:
        print("Requesting %s" % (url))
        r = requests.get(url)
        page = json.loads(r.content)
        items = page["results"]
        print("Retrieved %d items" % (len(items)))
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

def getItemList(urls):
    charList = []
    for url in urls:
        char = getItem(url)
        charList.append(char)
    printItems(charList, "name")



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
