import os
from bs4 import BeautifulSoup
import string
import re

def extract_link(node, class_name):
    link_icon = node.select(f"i[class*={class_name}]")
    if link_icon:
        link = link_icon[0].find_parent('a').get('href')
        link = '"' + link + '"'
    else:
        link = None
    return link


chars = re.escape(string.punctuation)

with open("/Users/gyt/publications.html.bak") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for div in soup.find_all("div", class_="row"):
    year = div.find("h4").text.strip()
    for li in div.find_all("li"):
        title = li.find("b").text.strip()
        title_short = "-".join(title.lower().split()[:3])
        title = title.replace('"', '')
        title = '"' + title + '"'

        month_icon = li.select("i[class*=fa-calendar]")
        if month_icon:
            month = month_icon[0].find_next_sibling(text=True).strip()
            month_num = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12"
            }[month[:3]]
        else:
            month = None
            month_num = "00"

        authors_icon = li.select("i[class*=fa-users]")
        if authors_icon:
            authors = authors_icon[0].find_next_sibling(text=True).strip()
            authors = '"' + authors + '"'
        else:
            author_p = li.find('p', string=lambda s: s and 'Abeed Sarker' in s)
            if author_p:
                authors = author_p.get_text(strip=True)
                authors = '"' + authors + '"'
            else:
                authors = None

        citation = li.find_all("div", class_="modal-content")[0].find("p").text.strip()
        citation = citation.replace('"', '')
        citation = '"' + citation + '"'

        # Extract links
        paper_link = extract_link(li, "fa-link")
        code_link = extract_link(li, "fa-code")
        resource_link = extract_link(li, "fa-tools")

        # Generate markdown file
        filename = "{}-{}-{}-{}.md".format(year, month_num, "01", re.sub('['+chars+']', '-', title_short))
        with open('_posts/'+filename, "w") as f:
            f.write("---\n")
            f.write("category: publication\n")
            f.write("layout: default\n")
            f.write("title: {}\n".format(title))
            f.write("link: {}\n".format(paper_link))
            f.write("year: {}\n".format(year))
            f.write("month: {}\n".format(month))
            f.write("author: {}\n".format(authors))
            f.write("citetxt: {}\n".format(citation))
            #f.write("resources: {}\n".format(resource_link)) # the source html has some errors
            #f.write("code: {}\n".format(code_link))
            f.write("---\n")

        print("Generated file: {}".format(filename))

