class Lamp:
  _LAMPS = ['''
    .----------.
    |   ~ON~   |
    |   ____   |
    |  |.--.|  |
    |  ||  ||  |
    |  ||__||  |
    |  ||\ \|  |
    |  |\ \_\  |
    |  |_\[0]  |
    |          |
    |  ~OFF~   |
    '----------'
    ''',
    '''
    .----------.
    |   ~ON~   |
    |   __     |
    |  | /[0]  |
    |  |/ / /  |
    |  ||/_/|  |
    |  ||  ||  |
    |  ||  ||  |
    |  |.__.|  |
    |          |
    |  ~OFF~   |
    '----------'
  ''']

  def __init__(self, _is_turned_on):
    self._is_turned_on = False

  def turn_on(self):
    self._is_turned_on = True
    self._display_image()

  def turn_off(self):
    self._is_turned_on = False
    self._display_image()

  def _display_image(self):
    if self._is_turned_on:
      print(self._LAMPS[1])
    else:
      print(self._LAMPS[0])

class Foco:
  pass