"""
suma.py

Description:
	Suma de tres números aleatorios

Authors:
	Joan Pont (jponte98@gmail.com)
	Gabriel Jaume (bieljaumemartin@gmail.com)

"""

import numpy as np

def main():
	# Obtenemos los números aleatorios
	x,y,z = np.random.rand(3)
	# Relizamos la suma
	suma = (x+y)+z
	# Imprimimos el resultado
	print("-"*90)
	print(f'SUMA: {suma}')
	print("-"*90)

if __name__ ==  "__main__":
	main()
