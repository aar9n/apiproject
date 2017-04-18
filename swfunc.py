import requests
import json

def getAllPages(url):
"""
When there are multiple pages pertaining to a single list of objects,
this function loads in all of the pages and extends the list. For example,
in swapi.co, there are 87 characters in the Star Wars universe. Because swapi.co
only returns 10 items at a time, getAllPages makes 9 requests.
"""
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
"""
Returns any single item with a url as a dictionary.
"""
    r = requests.get(url)
    item = json.loads(r.content)
    return item

def printItems(lst, key):
"""
Assigns sequential integers to each item in a list, printing the key attribute
of each item.
"""
    idx = 1
    for item in lst:
        print("%d. %s" % (idx, item[key]))
        idx = idx + 1

def getItemList(urls, name):
"""
Requests each individual url, taking their responses and putting them in a list.
It also prints an indexed list of the resources' name attributes.
"""
    itemList = []
    for url in urls:
        item = getItem(url)
        itemList.append(item)
    printItems(itemList, name)
    return itemList

def printAttributes(item):
"""
Takes the non-list attributes of a dictionary and prints them out in a formatted
manner. When printing the opening_crawl attribute of the "film" items, printAttributes
adds extra newlines.
"""
    for key in item:
        value = str(item[key])
        if key == 'opening_crawl':
            value = "\n" + value + "\n"
        if type(item[key]) is not list:
            print("%s: %s" % (key.title(), value))

def promptForItem(items, swType):
"""
The innermost while loop of swexplore. It prompts the user to explore a different
item or to return to a previous menu.
"""
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
