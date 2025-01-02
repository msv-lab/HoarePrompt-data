temp = raw_input()
temp_list = temp.split()
a = temp_list[0]
b = temp_list[1]
c = temp_list[2]

count = 0
for i in range(a,b):
  if c/i == 0:
    count += 1

print(count)
