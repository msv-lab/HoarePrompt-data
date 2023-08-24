s = input()
count = 0
distinct_people = 0

for char in s:
    if char == "+":
        count += 1
    else:
        count -= 1
        
    distinct_people = max(distinct_people, count)
    if count < 0:
        count = 0

print(distinct_people)