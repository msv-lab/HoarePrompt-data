s1 = raw_input()
s2 = raw_input()

print(sorted(s1))
print(sorted(s2))

dict1 = {}
dict2 = {}

for i in s1:
	dict1[i] = dict1.get(i,0)+1
for i in s2:
	dict2[i] = dict2.get(i,0)+1

values1 = sorted(dict1.values())
values2 = sorted(dict2.values())

for i in range(len(values1)):
	if values1[i]!=values2[i]:
		print("No")
print("Yes")