import re

def extract_quotation(string):
    # Use regular expression to find all substrings enclosed in double quotes
    return re.findall(r'"(.*?)"', string)

# Test cases
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []

# These tests should pass without any assertion errors.
