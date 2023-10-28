import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = "https://www.moe.gov.sg/schoolfinder?journey=Post%20secondary-JC%20school"


s = HTMLSession()
r = s.get(URL)

r.html.render(sleep = 1)

products = r.html.xpath('//*[@id="moe-school-finder"]', first = True)

print(products.absolute_links)

for item in products.absolute_links:
    schools = s.get(item)
    name = schools.html.find('table.moe-table--no-border', first=True).text
    print(name.split("Email: ",1)[1].split("Website")[0])
    