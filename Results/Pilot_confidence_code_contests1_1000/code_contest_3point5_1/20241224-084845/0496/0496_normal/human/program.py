import sys
l1=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
char=raw_input()
word=raw_input()
l=list(word)
j=0
if(char=='R'):
	for j in range(0,len(word)):
		for i in range(0,len(l1)):
			if(l1[i]==word[j]):
				sys.stdout.write(l1[i-1])
		
if(char=='L'):
	for i in range(0,len(l1)):
		if(l1[i]==word[j]):
			sys.stdout.write(l1[i+1])
			j=j+1

print