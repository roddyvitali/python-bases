import random
def run():
  number_found = False
  qty = int(input('Dime cuantos números tendrá esta lotería: '))
  print('Ya, lo tengo, la lotería tiene {} números'.format(qty))
  random_number = random.randint(0,qty)

  while not number_found:

    number = int(input('Ahora Intenta un número: '))

    if number == random_number:
      print('Felicidades. Encontraste el número')
      number_found = True
    elif number > random_number:
      print('El número es más pequeño')
    else:
      print('El número es más grande')

if __name__ == '__main__':
  run()