import bs4
from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.officequotes.net/no1-01.php")
soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup("div", class_="quote")

for item in quotes:
    quote = item.contents

    lines = []
    charac_lines = {}
    
    for subitem in quote:
        if isinstance(subitem, bs4.element.NavigableString) and subitem != ' ':
            print(subitem.string)
            lines.append(str(subitem.string))
        elif isinstance(subitem, bs4.element.Tag) and len(subitem) > 0:
            if not isinstance(subitem.contents[0], bs4.element.Tag):
                print(subitem.contents[0])
                lines.append(subitem.contents[0])
        else: pass
    break

print()
print(lines)

