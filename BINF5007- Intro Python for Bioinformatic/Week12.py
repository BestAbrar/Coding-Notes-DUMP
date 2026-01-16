#How to use data from external databases
#XML are human readable files (Markup Languages)
import xml.etree.ElementTree as ET
'''
#Reading XML file
tree = ET.parse("planets.xml")
root = tree.getroot()

for planet in root:
    for planet_element in planet:
        print(planet_element.tag, planet_element.text)
'''
#Making XML file
tree = ET.parse("books.xml")
root = tree.getroot()
'''
for book in root:
    for book_element in book:
        if book_element.tag == "title":
            title = book_element.text
        if book_element.tag == "year" and int(book_element.text)<2005:
            print(title)
'''
'''
for book in root:
    year_elem = book.find('year')
    if int(year_elem.text)<2005:
        print(book.find("title").text)
'''
#saving XML files 
'''
root = ET.Element('cities')
city_1 = ET.SubElement(root,'city')
name_c1 = ET.SubElement(city_1,'name')
name_c1.text = 'Toronto'
country_c1 =  ET.SubElement(city_1,'country')
country_c1.text = 'Canada'

tree = ET.ElementTree(root)
tree.write("cities.xml")
'''
import json
#opening and manipulating JSON files
'''
with open ("genes.json") as genes_file:
    data = json.load(genes_file)
    genes_list = data["genes"]

    for gene in genes_list:
        print(gene["name"])
'''
#Making a new JSON file
sports_teams = {"MLB":["Toronto Blue Jays",
                       "New York Mets",
                       "Boston Red Sox"],
                "NBA":["Toronto Raptors",
                       "Miami Heat",
                       "Boston Celtics"]
                }
with open ("teams.json","w") as outfile:
    json.dump(sports_teams, outfile)