from bs4 import BeautifulSoup

# Note recent updates require specifying the encoding to avoid a UnicodeDecodeError.
# The open function encoding option is platform dependent, and may not be utf-8.
# Therefore an error can occur when using read on a file which is utf-8 but open is using ascii.
with open("website.html", "r", encoding='utf-8') as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)  # print the full title element
print(soup.title.name)  # print the name of the title element
print(soup.prettify())  # print the full html with indentation
all_anchor_elements = soup.find_all(name="a")  # return all anchor elements

# print all href from anchor elements
for element in all_anchor_elements:
    print(element.get("href"))

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))