entrada = list(raw_input().split())
ligacao = list(raw_input().split())
result = []
saida = ''
ligacao.append('fim')

for i in ligacao:
	if(i == 'fim'):
		break
	if(len(result) != len(set(result))):
		result.remove(result[0])
	else:	
		result.insert(0,i)	
	if(len(result) > int(entrada[1])):		
		result.remove(result[int(entrada[1])])
		
if(len(result) != len(set(result))):
		result.remove(result[0])

for i in range(len(result)):
	saida += str(result[i])
	if(i < len(result)):
		saida += ' '
		
print(len(result))
print(saida)




		      	     			 	  		  			  	