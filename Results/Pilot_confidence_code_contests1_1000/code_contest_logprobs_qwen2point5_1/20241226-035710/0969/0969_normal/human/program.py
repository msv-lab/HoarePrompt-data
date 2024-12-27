quant = int(raw_input())
valores = map(int, raw_input().split(" "))

for i in valores:
	distancias = []
	aux = valores[::]
	aux.remove(i)
	
	if (abs(i - min(aux)) > abs(i - max(aux))):
		print(str(abs(i - max(aux)))+ " " + str(abs(i - min(aux))))
	else:
		print(str(abs(i - min(aux)))+ " " + str(abs(i - max(aux))))
	
	
