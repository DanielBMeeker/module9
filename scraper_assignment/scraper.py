"""
Program: scraper.py
Author: Daniel Meeker
Date: 6/30/2020

This program takes in a URL and scrapes the information from it
and writes the HTML code to two different files. One of the files
is all on one line while the other is formatted to be more human
readable.
"""
import requests
import bs4


url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202101&Campus=1&Subject=CIS'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()
soup = bs4.BeautifulSoup(open("requestResult.txt"), 'html.parser')
f = open('requestResultsPretty.txt', 'w+')
f.writelines(soup.prettify())
f.close()
