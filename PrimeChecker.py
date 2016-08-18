class PrimeChecker(object):
  
  def __init__(self, number=""):
    self.number = number
    
  def is_prime(self):
    
    if self.number == "":
      return False
    elif int(self.number) > 1:
      for i in range(2,(int(self.number))):
        if not (int(self.number)%i):
          return False
      else:
          return True