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
