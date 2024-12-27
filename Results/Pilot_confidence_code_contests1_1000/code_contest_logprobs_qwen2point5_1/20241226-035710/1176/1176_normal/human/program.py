gogol = raw_input()
pineapple = raw_input()

gogol = gogol.replace(pineapple, '#')
count = 0

for char in gogol:
    if char == '#':
        count += 1

print(count)

      			   	    		   			 			 	