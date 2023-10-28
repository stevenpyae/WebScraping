from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re

service = Service()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(service=service, options=chrome_options)
# Query to obtain links

with open('jcs.txt', 'r') as file:
    lines = file.readlines()

//print(lines)
queries = ["Exeter Maths School"]

noneQuery = []
links = [] # Initiate empty list to capture final results
# Specify number of pages on google search, each page contains 10 #links
for query in lines:
    url = "http://www.google.com/search?q=" + query + 'UK email address'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')
    # Find Links
    # search_result = soup.find('div', class_="yuRUbf").find('a').get("href")

    # Search by first google results get the email
    search_result = soup.find('div', class_="VwiC3b yXK7lf yDYNvb W8l4ac lyLwlc lEBKkf").find(string=re.compile(".ac.uk"))
    if search_result is None:
        print(query + " : None" )
    else:
        print(query + " : " + search_result)

#print(noneQuery)
#                
## Open another page 
#for query in noneQuery:
#    regex = ''.join(query.split("www.")[1].split("/contact"[0]))
# #   driver.get(noneQuery)
# #   soupy = soup = BeautifulSoup(r.text, 'html.parser')
# #   search_result = soupy.find(string = re.compile(""))
## Find the reference @ac.uk
