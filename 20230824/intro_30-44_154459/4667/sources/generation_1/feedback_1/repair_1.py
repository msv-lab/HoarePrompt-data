import xml.etree.ElementTree as ET

def get_element_score(element):
    score = len(element.attrib)
    for child in element:
        score += get_element_score(child)
        score += len(child.attrib)
    return score

# Read input
N, xml = input().split(maxsplit=1)

# Add root element to the XML string
xml_string = "<root>\n" + xml + "\n</root>"

# Construct XML tree
root = ET.fromstring(xml_string)

# Calculate score
score = get_element_score(root)

# Print score
print(score, end="")