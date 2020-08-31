import bs4
import requests
url = "https://jadwalsholat.pkpu.or.id/?id=266"
contents = requests.get(url)
responses = bs4.BeautifulSoup(contents.text,"html.parser")
data = responses.find_all("tr","table_highlight")
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat["subuh"] = d.get_text()
    elif i == 2:
        sholat["dhuhur"] = d.get_text()
    elif i == 3:
        sholat["ashar"] = d.get_text()
    elif i == 4:
        sholat["maghrib"] = d.get_text()
    elif i == 5:
        sholat["isya"] = d.get_text()
    i += 1
print(sholat)
