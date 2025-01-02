def magic(number):
	return str(''.join(str(i) for i in number))
n=int(raw_input())
s=raw_input()
stack=[]
vowel=['a','e','i','o','u']
for i in range(len(s)):
	if(i==0):
		stack.append(s[i])
	else:
		if((stack[len(stack)-1] in vowel) and (s[i] in vowel)):
			continue

		else:
			stack.append(s[i])
	
			
print(magic(stack))

