i = map(int, raw_input().split(" "))


def get_time(params):
	assigned = 1
	total = params[1]

	while assigned < params[0]:
		double = assigned * 2
		# No se puede doblar la cantidad
		if double > params[0]:
			# Al total le anyadimos las letras sobrantes por el tiempo necesario por letra
			return total + (params[0] - assigned) * params[1]
		# Existe la posibilidad de doblar la cantidad
		else:
			# Si el coste de doblarlo es menor que el de anyadir una a una lo doblamos
			one_cost = assigned * params[1]
			if one_cost > params[2]:
				total += params[2]
				assigned *= 2
			else:
				total += params[1]
				assigned += 1
	return total

print(get_time(i))
