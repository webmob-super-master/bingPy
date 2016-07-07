#! /usr/bin/env python3

import webbrowser, time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','bb','cc','dd']

for i in range(0,30):
    time.sleep(1)
    webbrowser.open('https://www.bing.com/search?q=' + alphabet[i])

