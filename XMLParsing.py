__author__ = 'Dana'
import xml.etree.ElementTree as ET

path = "C:\Temp\AAA\\TEST.xml"

tree = ET.parse(path)
root = tree.getroot()

# print(root.tag)

for child in root:
    print(child.tag, child.attrib)
    for sub in child:
        print("\t", sub.tag, sub.attrib, sub.text)
    print()


# ET.dump(root)