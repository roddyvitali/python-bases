#Empezamos con python 3.7
import math

def is_prime(number):
	if number < 2:
		return False
	sq_root = int(math.sqrt(number))
	for i in range( 2, sq_root+1):
		if number % i ==0:
			return False
	return True

def run():
  number = int(input('Escribe un número: '))
  result = is_prime(number)

  if result is True:
    print('Tu número es primo')

  else:
    print('Tu número NO es primo')

if __name__ == '__main__':
  run()