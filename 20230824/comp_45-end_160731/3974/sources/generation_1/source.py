s = input()
count = 0
distinct_people = 0

for char in s:
    if char == "+":
        count += 1
        distinct_people = max(distinct_people, count)
    else:
        count -= 1

print(distinct_people)