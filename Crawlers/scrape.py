import requests
from bs4 import BeautifulSoup

url ="https://royalenfield.com/locateus/dealers/"
r= requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	# if "http" in link.get("href"):
	print ( "a <href = '%s'>%s</a>" %(link.get("href"),link.text))


g_data = soup.find_all("div" , {"class": "addrContainer"})

for item in g_data:
	print(item.contents)
