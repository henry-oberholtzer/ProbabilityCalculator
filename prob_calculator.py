import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.contents.extend([key for _ in range(value)])
  def draw(self, amount):
    draws = []
    for _ in range(amount):
        length = len(self.contents)
        if length == 0:
          break
        elif length == 1:
          draw = self.contents[0]
        else:
          draw = self.contents[random.randint(1, length) - 1]
        self.contents.remove(draw)
        draws.append(draw)
    return draws


def experiment(hat:Hat, expected_balls:dict, num_balls_drawn, num_experiments):
  success = 0
  for _ in range(num_experiments):
    draw = hat.draw(num_balls_drawn)
    if all([True if v >= draw.count(k) else False for k, v in expected_balls.items()]):
      success += 1
  return success / num_experiments
