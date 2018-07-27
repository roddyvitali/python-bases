import random
import os

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
  'python',
  'php',
  'java',
  'javascript',
  'reactjs',
  'nodejs',
  'express',
  'mongodb',
  'angularjs',
  'angular',
  'ionic',
  '.net',
  'vuejs',
  'react-native',
  'laravel',
  'ruby',
  'rails',
  'django'
]

def random_word():
  idx = random.randint(0, len(WORDS) -1)
  return WORDS[idx]

def display_board(hidden_word, tries, letters_used):
  os.system('cls' if os.name=='nt' else 'clear')
  print('B I E N V E N I D O S   A   A H O R C A D O S')
  print(IMAGES[tries])
  print('')
  print('LETRAS UTILIZADAS')
  print(letters_used)
  print('')
  print('PALABRAS A ENCONTRAR')
  print(hidden_word)
  print('--- * --- * --- * --- * ---')

def run():
  word = random_word()
  hidden_word = ['-'] * len(word)
  letters_used = []
  tries = 0

  while True:
    display_board(hidden_word, tries, letters_used)
    current_letter = str(input('Escoge una letra: '))

    letter_indexes = []
    for idx in range(len(word)):
      if word[idx] == current_letter:
        letter_indexes.append(idx)

    if current_letter in letters_used:
      print('')
      print('Ya usaste la letra {}'.format(current_letter))
      # display_board(hidden_word, tries, letters_used)
    else:
      letters_used.append(current_letter)

      if len(letter_indexes) == 0:
        tries += 1

        if tries == 6:
          display_board(hidden_word, tries, letters_used)
          print('')
          print('¡Perdiste! La palabra correcta era {}'.format(word))
          break
      else:
        for idx in letter_indexes:
          hidden_word[idx] = current_letter

        letter_indexes = []

      try:
        hidden_word.index('-')
      except ValueError:
        print('')
        print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
        break

if __name__ == '__main__':
  run()