import xml.etree.ElementTree as ET

def get_element_score(element):
    score = len(element.attrib)
    for child in element:
        score += get_element_score(child)
    return score

# Read input
N = int(input())
xml_lines = [input() for _ in range(N)]

# Construct XML tree
xml_string = '\n'.join(xml_lines)
root = ET.fromstring(xml_string)

# Calculate score
score = get_element_score(root)

# Print score
print(score)