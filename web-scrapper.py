from bs4 import BeautifulSoup
import requests

#opens html from file
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#tags = doc.find_all("p")[0]
#print(tags.find_all("b"))

#opens html from website (if the item is out of stock and price does not appear on the website, there will be an error thrown)
url = "https://www.newegg.ca/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)