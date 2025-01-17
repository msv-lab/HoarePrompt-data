def unique_Element(lst):
    return len(set(lst)) == 1

# Testing the function with the provided test cases
assert unique_Element([1,1,1]) == True
assert unique_Element([1,2,1,2]) == False
assert unique_Element([1,2,3,4,5]) == False
