# 
# File Name: AcroSensei
# Version: 1.0
# Author: Justin Luo
# Last Updated: 6/3/2023
# This is the first version of AcroSensei, an easy to use tool to help people 
# look up acronym definitions using web crawler technology
#
import requests
import bs4
import re

# Taking user input
x = input("What is your acronym? ")

# Convert the inputted acronym to lowercase
x = x.lower()

# Constructing the URL based on the user input
URL = f"https://en.wikipedia.org/wiki/List_of_acronyms:_{x[0].upper()}"

# Sending a GET request to the URL
res = requests.get(URL)

# Checking if the request is successful
if res.status_code == 200:
    # Extracting information from the page using BeautifulSoup
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Get the page content as text
    page_text = soup.get_text().lower()

    # Searching for the inputted acronym within the page text
    found_definitions = []
    
    for li in soup.find_all("li"):
        acronym_text = li.text.strip().lower()
        new_acronym = ''
        if acronym_text.startswith(x) and x in acronym_text.split():
            # Remove text within parentheses using regular expressions
            new_acronym = re.sub(r'\([^()]*\)', '', acronym_text)
            final_acronym = new_acronym.strip()
            found_definitions.append(final_acronym)

    # Sort the definitions in alphabetical order
    found_definitions.sort()

    # Printing the definitions of the specific inputted acronym
    if found_definitions:
        print("Definitions:")
        for definition in found_definitions:
            print("- " + definition)
    else:
        print("No definition found for the given acronym.")
else:
    print("This page does not exist.")
