from tire.tire import Tire

class OctiprimeTire(Tire):
  def __init__(self, worn_level):
    self.worn_level = worn_level
  
  def needs_service(self):
    sum = 0
    for index in self.worn_level:
      sum += index
      if sum >= 3:
        return True
    return False