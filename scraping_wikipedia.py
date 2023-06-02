import requests
import bs4


URL = "https://en.wikipedia.org/wiki/List_of_acronyms:_Q"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

res = requests.get(URL, headers=headers)
print(res.status_code)  # 200

soup = bs4.BeautifulSoup(res.text, features="html.parser")
# acronym_list = soup.find_all("div", class_="div-col div-col-rules")
acronym_list = soup.find_all("div", class_= "vector-body ve-init-mw-desktopArticleTarget-targetContainer")

for acronym in acronym_list:
    print(acronym.text)