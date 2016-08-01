#! /usr/bin/env python3

import webbrowser, time

searchTerm = []

for i in range(0,30):
    searchTerm.append(str(i))
    time.sleep(1)
    webbrowser.open('https://www.bing.com/search?q=' + searchTerm[i])
