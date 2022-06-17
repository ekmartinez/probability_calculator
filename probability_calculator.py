import random
import copy

class Hat:
  def __init__(self, **kwargs): 
    self.arguments = []
    
    for key, value in kwargs.items():
      self.arguments.extend([key] * value) 
    
    self.contents = copy.deepcopy(self.arguments)

  def draw(self, sample):
    resultList = []
    self.contents = copy.deepcopy(self.arguments)
    for selection in range(sample):
      if len(self.contents) < 1:
        self.contents = copy.deepcopy(self.arguments)
      s = random.choice(self.contents)
      self.contents.remove(s)
      resultList.append(s)
    return resultList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0 
  for t in range(num_experiments):
    draw = hat.draw(num_balls_drawn)
    testCheck = 0
    for k, v in expected_balls.items():
      if draw.count(k) >= expected_balls[k]:
        testCheck += 1
    if testCheck >= len(expected_balls.keys()):
      m += 1
            
  return m / num_experiments