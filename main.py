import xml.etree.ElementTree as ET
tree = ET.parse("cabs_piano_oboe_v3.xml")
root = tree.getroot()

"""
print(root.tag, root.attrib)
for child in root:
    print(child.tag, child.attrib, child.text)
"""

# Find title, author, copyright year
title = root.findall("./movement-title")[0].text
author = root.findall("./identification/creator")[0].text
copyright = root.findall("./identification/rights")[0].text

# Find part list
parts = root.findall("./part-list")
partList = []
for child in parts: # part list
    for i in range(len(child)):
        tag = child[i].tag
        if tag == 'part-group':
            pass
        else:
            attribList = child[i].attrib
            keyList = list(attribList.keys())
            for key in keyList:
                partList.append(attribList[key])
                #print(attribList[key])

# Find 1 part, partList[0]
partId = partList[0]
part = root.findall("./part[@id='P1']")
print(part)
print(type(part))


# Prints
print(title)        # title
print(author)       # author
print(copyright)    # copyright
print(partList)     # part list
