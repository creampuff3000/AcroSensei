import requests
import bs4

# taking user input
x = input("What is your acronym? ")

# comparing user input to each list to find out which URL to use
URL = f"https://en.wikipedia.org/wiki/List_of_acronyms:_{x[0]}"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

# use URL to get page
res = requests.get(URL, headers=headers)

# checks if request is successful
if res.status_code == 200:
    print(res.status_code)
else:
    print("This page does not exist.")
    exit(0)

# extract information from page using beautifulsoup
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# looking for text with class div
acronym_list = soup.find_all("div", title = str(x))

# printing acronyms in a list
for acronym in acronym_list:
    print(acronym.text)