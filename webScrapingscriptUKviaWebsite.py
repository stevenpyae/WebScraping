from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
service = Service()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(service=service, options=chrome_options)
# Query to obtain links
queries = [
"Harris Westminster Sixth Form",
"Sir Isaac Newton Sixth Form",
"Brighton Hove and Sussex Sixth Form College (BHASVIC)",
"Harington School",
"London Academy of Excellence Tottenham",
"Sir John Deane’s Sixth Form College",
"Chapeltown Academy",
"Kimberley Sixth Form College",
"Richard Huish College",
"King Edward VI College Stourbridge",
"Prior Pursglove College",
"East Norfolk Sixth Form College",
"Melton Vale Sixth Form College",
"Marple Sixth Form College",
"Elliott Hudson College",
"Solihull Sixth Form College",
"King Edward VI College, Nuneaton",
"City of Stoke-On-Trent Sixth Form College",
"Richard Taunton Sixth Form College"]

noneQuery = []
links = [] # Initiate empty list to capture final results
# Specify number of pages on google search, each page contains 10 #links
for query in queries:
    url = "http://www.google.com/search?q=" + query + 'UK email address'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')
    search_result = soup.find('div', class_="yuRUbf").find('a').get("href")

    if search_result is None:
        print(query + " : None" )
    else:
        noneQuery.append(search_result)
        print(query + " : " + search_result)

for links in noneQuery:
    regex = ''.join(query.split("https://www.")[1].split("/contact"[0]))
    driver.get(links)
    soupy = BeautifulSoup(driver.page_source, 'html.parser')
    searchy = soupy.find(string=re.compile(regex))