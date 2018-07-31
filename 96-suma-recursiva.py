def sum(number):
  if number == 0:
    return 0
  
  return number + sum(number - 1)

if __name__ == '__main__':
  print('S U M A   F A C T O R I A L')
  num = int(input('¿Cuántos números deseas sumar: '))
  result = sum(num)
  print('El resultado de la suma recursiva es: {}'.format(result))


