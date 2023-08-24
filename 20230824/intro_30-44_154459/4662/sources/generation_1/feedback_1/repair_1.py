def calculate_max_nesting(xml_doc):
    max_level = 0
    current_level = 0
    for line in xml_doc:
        prev_char = ""
        for char in line:
            if char == "<":
                if prev_char == "/":
                    # Handling self-closing tags
                    continue
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == "/" and prev_char == "<":
                # Identifying end tags
                current_level -= 1
            prev_char = char
    return max_level

# Read input
n = int(input())
xml_doc = []
for _ in range(n):
    xml_doc.append(input())

# Calculate and print the maximum level of nesting
max_nesting = calculate_max_nesting(xml_doc)
print(max_nesting)