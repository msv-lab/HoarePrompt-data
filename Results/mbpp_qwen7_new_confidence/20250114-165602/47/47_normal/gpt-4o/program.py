def index_minimum(lst):
    if not lst:
        return None  # Handle the edge case where the list is empty
    return min(lst, key=lambda x: x[1])[0]

# Testing the function with the provided test cases
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
