binary_base = [1, 2, 4, 8, 16, 32, 64, 128]

def cypher(message):
    cypher_words = []
    for letter in message:
        cypher_letter = format( ord(letter), 'b' )
        cypher_words.append(cypher_letter)

    return' '.join(cypher_words)


def decipher(message):
    words = message.split(' ')
    decipher_message = []
    for word in words:
        word = str(word)
        sumatory = 0
        for value, letter in enumerate(word[::-1]):
            if int(letter) == 1:
                sumatory += binary_base[value]
        decipher_letter = chr(sumatory)
        decipher_message.append(decipher_letter)

    return"".join(decipher_message)


def run():

  while True:

    command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
      Bienvenido a criptografía. ¿Qué deseas hacer?

      [c]ifrar mensaje
      [d]ecifrar mensaje
      [s]alir
    '''))

    if command == 'c':
      message = str(input('Escribe un mensaje: '))
      cypher_message = cypher(message)
      print(cypher_message)
    elif command == 'd':
      message = str(input('Escribe un mensaje: '))
      decipher_message = decipher(message)
      print('')
      print(decipher_message)
    elif command == 's':
      exit()
    else:
      print('¡Comando no encontrado!')


if __name__ == '__main__':
  print('M E N S A J E S  C I F R A D O S')
  run()