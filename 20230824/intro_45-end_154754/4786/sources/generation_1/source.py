
def filter_keywords(n, keywords):
    filtered_keywords = set()
    for keyword in keywords:
        normalized_keyword = keyword.lower().replace("-", " ")
        filtered_keywords.add(normalized_keyword)
    return len(filtered_keywords)

# Read input
n = int(input())
keywords = [input() for _ in range(n)]

# Call the function to get the result
result = filter_keywords(n, keywords)

# Print the result
print(result)
