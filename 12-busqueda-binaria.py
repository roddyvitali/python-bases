def binary_search(number, number_to_find, low, high):
  if low > high:
    return False

  mid = int( (low + high) / 2 )
  print(mid)

  if numbers[mid] == number_to_find:
    return True
  elif numbers[mid] > number_to_find:
    return binary_search(numbers, number_to_find, low, mid - 1)
  else:
    return binary_search(numbers, number_to_find, mid + 1, high)
  

if __name__ == '__main__':
  numbers = [3, 5, 6, 21, 22, 23, 28, 31, 34, 36, 39, 41, 44, 52, 56, 59, 66, 74, 90, 94]
  #numbers_sort = numbers.sort
  number_to_find = int(input('Ingresa un número: '))
  result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

  if result is True:
    print('El número sí está en la lista.')
  else:
    print('El número NO está en la lista.')
