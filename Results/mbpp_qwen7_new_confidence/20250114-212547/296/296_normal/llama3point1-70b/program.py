def extract_quotation(s):
    result = []
    in_quote = False
    current_quote = ""
    for char in s:
        if char == '"':
            if in_quote:
                result.append(current_quote)
            in_quote = not in_quote
            current_quote = ""
        elif in_quote:
            current_quote += char
    return result
