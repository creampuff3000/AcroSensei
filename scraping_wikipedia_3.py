import requests
import bs4

# Taking user input
x = input("What is your acronym? ")

# Constructing the URL based on the user input
URL = f"https://en.wikipedia.org/wiki/List_of_acronyms:_{x[0]}"

# Sending a GET request to the URL
res = requests.get(URL)

# Checking if the request is successful
if res.status_code == 200:
    # Extracting information from the page using BeautifulSoup
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Looking for definition elements within li tags
    definitions = soup.find_all("li")

    # Printing the definitions of the acronyms
    found_definitions = False
    for li in definitions:
        if li.text.strip().startswith(x):
            found_definitions = True
            print(li.text.strip()) # returns copy of string without first and last letter

    if not found_definitions:
        print("No definitions found for the given acronym.")
else:
    print("This page does not exist.")
