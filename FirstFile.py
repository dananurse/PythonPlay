import xml.etree.ElementTree as ET

myfile = "C:\Temp\AAA\\file.txt"

print(myfile)

FILE = open(myfile, 'w')

for x in range(0, 3):
    FILE.writelines("Line number " + str(x) + "\n")

FILE.close()

root = ET.Element("A")
ET.SubElement(root, "B")
ET.dump(root)