def calculate_max_nesting(xml_doc):
    max_level = 0
    current_level = 0
    for line in xml_doc:
        for char in line:
            if char == "<":
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ">":
                current_level -= 1
    return max_level

# Read input
n = int(input())
xml_doc = []
for _ in range(n):
    xml_doc.append(input())

# Calculate and print the maximum level of nesting
max_nesting = calculate_max_nesting(xml_doc)
print(max_nesting)