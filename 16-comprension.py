pairs = []
for num in range(1,31):
  if num % 2 == 0:
    pairs.append(num)
print(pairs)
#list comprehension
list_items = [num for num in range(1, 31)] 
print(list_items)

even = [num for num in range(1,31) if num % 2 == 0]
print(even)

square = {}
for num in range(1, 11):
  square[num] = num**2
#dictionary comprehension
print(square)

squares = { num: num**2 for num in range(1, 11) }
print(squares)
