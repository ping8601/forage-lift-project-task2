from tire.tire import Tire

class CarriganTire(Tire):
  def __init__(self, worn_level) :
    self.worn_level = worn_level

  def needs_service(self):
    for index in self.worn_level:
      if index >= 0.9:
        return True
    return False