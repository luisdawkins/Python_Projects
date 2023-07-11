from bs4 import BeautifulSoup
import requests

#Stores target URL
URL = "https://www.newegg.ca/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771"

#Configuration
Results = requests.get(URL)
Document = BeautifulSoup(Results.text, "html.parser")

def Return_Price_of_GPU():
    #String manipulation to output price of GPU
    #Retrieve all strings containing '$'
    Prices = Document.find_all(string="$")
    #Returns parent tag
    Parent = Prices[0].parent
    #Isolates the string value of parent tag
    Strong = Parent.find("strong")
    print("GPU Price($): " + Strong.string)

def Return_Model():
    Model_Name = Document.find_all(string = "Model")
    Parent_Tag = Model_Name[1].parent
    Parent_Tag = Parent_Tag.parent
    td = Parent_Tag.find("td")
    td = td.string
    print("GPU Model unit: " + td)

Return_Model()
Return_Price_of_GPU()
