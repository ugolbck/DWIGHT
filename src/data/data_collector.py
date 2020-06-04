import bs4
from bs4 import BeautifulSoup
import requests
import re
import html

# End product:
# 1 json (?) file as a dictionary with:
#       -> for each character, a list of question-answer pairs

# TODO
# make sure that only character names can go though the selector

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
    for i, subitem in enumerate(quote):
        
        # Encountering text
        if isinstance(subitem, bs4.element.NavigableString) and subitem != ' ':
            element = preprocess_line(str(subitem.string))
        
        # Encountering a `b` Tag
        elif isinstance(subitem, bs4.element.Tag) and subitem.name == 'b':
            print(subitem)
            # Verifies that the element is not a `<u> Deleted Scene </u>`
            if not isinstance(subitem.contents[0], bs4.element.Tag):
                
                # Last character is a column `:`
                element = str(subitem.contents[0][:-1])

                
            else: 
                continue
        
        else: 
            continue
        
        # Every second element is a character/line
        if i%2 != 0:
            characters.append(element)
        else:
            lines.append(element)

    return characters, lines


def looper(quotes):
    all_lines = []
    for item in quotes:
        quote = item.contents
        characters, lines = extract(quote)

        # if len(characters) != len(lines):
        # print(characters)
        # print(lines)
        # print()
            
        


def main():
    page = requests.get("https://www.officequotes.net/no2-10.php")
    soup = BeautifulSoup(page.content, 'html.parser')
    quotes = soup("div", class_="quote")

    looper(quotes)


main()