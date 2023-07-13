from bs4 import BeautifulSoup
import requests

#Configuration
URL = ["https://www.worldometers.info/gdp/gdp-by-country/#:~:text=GDP%20by%20Country%20%20%20%20%23%20,%20%204.56%25%20%2022%20more%20rows%20", "https://www.worldometers.info/gdp/gdp-per-capita/", "https://worldpopulationreview.com/country-rankings/health-care-costs-by-country"]
Full_HTML = requests.get(URL[0]).text
Soup = BeautifulSoup(Full_HTML, "html.parser")

#Retrieving table body
tbody = Soup.find("tbody")
trs = tbody.contents

#Remove spaces from list
for row in trs:
    if row == " ":
        trs.remove(" ")

#list top ten countries with GDP
for i in range(10):
    Nation = trs[i].find("a").string
    Nation_GDP = trs[i].find_all("td")[2].string
    print(Nation + ": " + Nation_GDP )
