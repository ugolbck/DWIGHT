# Deprecated file
# Data was obtained and organized elsewhere

import bs4
from bs4 import BeautifulSoup
import requests
import re
import html

# End product:
# 1 json (?) file as a dictionary with:
#       -> for each character, a list of question-answer pairs


def preprocess_line(text):
    # Remove `\t` from text
    text_preproc = re.sub('\s+', ' ', text)

    # Remove last character if empty space
    if text_preproc[-1] == ' ':
        text_preproc = text_preproc[:-1]

    # Remove first character if empty space
    if text_preproc[0] == ' ':
        return text_preproc[1:]
    return text_preproc

def preprocess_char(text):
    # Removing HTML escape characters
    # ex. "&amp;" -> "&"
    return html.unescape(text)


def extract(quote):
    # Processing a scene
    lines = []
    characters = []
    everything = []
    print(len(quote)); print(quote); print()
    for i, subitem in enumerate(quote):
        
        # Encountering text
        if isinstance(subitem, bs4.element.NavigableString) and subitem != ' ':
            preproc_subitem = preprocess_line(str(subitem.string))
            
            # Check that the line is not a direction line
            # if preproc_subitem[0] == '[' and preproc_subitem[-1] == ']':
            #     element = preproc_subitem
            #     print(element)

        # Encountering a `b` Tag
        elif isinstance(subitem, bs4.element.Tag) and subitem.name == 'b':
            
            # Verifies that the element is not a `<u> Deleted Scene </u>`
            if not isinstance(subitem.contents[0], bs4.element.Tag):
                
                # Sometimes there is an extra HTML tag, so I give up the character name
                if len(subitem.contents) > 1:
                    element = "PLACEHOLDER"
                else:
                    # Last character is a column `:` so we do not take it
                    element = str(subitem.contents[0][:-1])
            else: 
                continue
        
        else: 
            continue
        
        # Every second element is a character/line
        if i%2 != 0:
            everything.append(element)
        else:
            everything.append(element)
        
    # print(everything)
    # print(everything[::2])

    return characters, lines


def looper(quotes):
    all_lines = []
    for item in quotes:
        quote = item.contents
        characters, lines = extract(quote)
        

        # if len(characters) == len(lines):
        #     print("characters:", characters)
        #     print("lines:", lines)
        #     print()
            
            
        


def main():
    page = requests.get("https://www.officequotes.net/no3-12.php")
    soup = BeautifulSoup(page.content, 'html.parser')
    quotes = soup("div", class_="quote")

    looper(quotes)


main()