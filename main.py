import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import re

#webcrawler challenge
def getwordscount(wordlimit=10,avoidlist = {}) -> None:

    regex = re.compile(r'<[^>]+>')

    def remove_html(string):
        return regex.sub('', string)
# look only in the history portion
    content = requests.get('https://en.wikipedia.org/wiki/Microsoft#History')

    histcontent1 = content.text.split(
        "<span class=\"mw-headline\" id=\"History\">")[1]
    histcontent = histcontent1.split(
        "<span class=\"mw-headline\" id=\"Corporate_identity\">")[0]

    cleancontent = remove_html(histcontent)

    wordcounts = {}
    with open('text.txt', 'w') as f:
        f.write(cleancontent)

    with open('text.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if word in wordcounts.keys():
                    wordcounts[word] += 1
                else:
                    wordcounts[word] = 1

    for each in avoidlist:
        try:
            wordcounts.pop(each)
        except:
            continue

    dictfinal = sorted(wordcounts.items(), key=lambda x: x[1])

    print(tabulate(dictfinal[len(dictfinal)-wordlimit:len(dictfinal)], headers=['word','# of occurrences'], tablefmt='fancy_grid'))



#getWords()
getwordscount(10, ['Windows', 'with', 'on'])
