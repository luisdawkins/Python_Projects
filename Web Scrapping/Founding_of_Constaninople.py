from bs4 import BeautifulSoup
import requests
import re

URL = "https://en.wikipedia.org/wiki/Constantinople"

Results = requests.get(URL)
Document = BeautifulSoup(Results.text, "html.parser")

def Find_Year_of_Founding(Debug_Info):
    if Debug_Info:
        #Finding a value the long way
        tags = Document.find_all(string="Founded")
        print(tags)
        Parent_tags = tags[0].parent
        print(Parent_tags)
        Parent_tags = Parent_tags.parent
        print("Here is the ultimate parent tag that includes the value needed to retrieve.")
        print(Parent_tags)
        Year_of_Founding = Parent_tags.find(class_ = "infobox-data")
        print(Year_of_Founding.string)
    elif not Debug_Info:
        tags = Document.find_all(string="Founded")
        Parent_tags = tags[0].parent
        Parent_tags = Parent_tags.parent
        Year_of_Founding = Parent_tags.find(class_ = "infobox-data")
        print(Year_of_Founding.string)

Find_Year_of_Founding(False)
