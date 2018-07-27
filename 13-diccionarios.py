def run():
  scores = {}
  scores['algoritmos'] = 9
  scores['matematicas'] = 10
  average = 0

  for key,value in scores.items():
    print('key: {}, value: {}'.format(key, value))
    average += value
  print('El promedio es: {}'.format(average/len(scores) ) )
if __name__ == '__main__':
  run()