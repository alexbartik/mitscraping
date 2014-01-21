import urllib
# from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup

def downloadpage(url, filename):
    page = urllib.urlretrieve (url, filename)  
    return page

def parsepage(filepath):
    with open(filepath) as page:
        soup = BeautifulSoup(page.read())
        pubs = soup.find("div", id = "subnavinfotype")
        links = pubs.find_all('a')
        
        titles = []
        for link in links:
            titles.append(link)

        return links

def writepage(links, datapage, faculty):
    with open(datapage, "w") as f:
        for link in links:
            line = faculty + "\t" + link.text  + "\n"
            f.write(line)


# Set Parameters
faculty = "acemoglu"
url = "http://economics.mit.edu/faculty/" + faculty + "/publication/"
datapage = "datapage.csv"

# Download Page
downloadpage(url, faculty + ".html")

# Parse Page
links = parsepage(faculty + ".html")

# Write page
writepage(links, datapage, faculty)
