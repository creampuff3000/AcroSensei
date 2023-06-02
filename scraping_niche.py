import requests
import bs4


URL = "https://www.niche.com/k12/search/best-schools/"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

res = requests.get(URL, headers=headers)
print(res.status_code)  # 200

soup = bs4.BeautifulSoup(res.text, features="html.parser")
highschools = soup.find_all("div", class_="card__inner")

for highschool in highschools:
    name = highschool.find("h2").text
    print(name)