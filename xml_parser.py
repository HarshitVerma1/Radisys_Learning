import xml.etree.ElementTree as ET
tree = ET.parse("country_data.xml")
root = tree.getroot()
print(root.tag)
# print(root.attrib)
# print(root[0][0].text)
# # root = ET.fromstring(country_data_as_string)
# print(root[0].attrib)
# print(root[0][0].attrib)


# for child in root:
#     print(child.tag)
#     print(child.attrib)

# for country_detail in root.iter('country'):
#     name = country_detail.get('name')
#     print("Name:{} ".format(name), end="   ")
#     print("Rank is : ", country_detail.find('rank').text)

# Modifying an xml file
# for country in root.iter('country'):
#     if country.get('name') == "Singapore":
#         country.find('rank').text = str(999)
#         country.find('year').text = str(2022)
# country.find('neighbor').set('name', 'India')
# country.find('neighbor').set('direction', 'North-West')

for country in root.findall('country'):
    countryName = country.find('neighbor').get('name')
    if countryName == 'India':
        root.remove(country)

tree.write("out.xml")
