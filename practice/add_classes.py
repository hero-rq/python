class Calculator:
  def __init__(self):
    self.result = 0
  def add(self, num):
    self.result += num
    return self.result

  def sub(self, num):
    self.result -= num
    return self.result

cal1 = Calculator()
s = cal1.add(17)
print(s)
