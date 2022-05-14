class Car(): 
  
   def __init__(self, **kwargs):
     self.wheels = 4
     self.windows = 4 
     self.doors = 4 
     self.seats = 4 
     self.color = kwargs.get("color", "black")
     self.price = kwargs.get("price", "$11") 

   def __str__(self):
     return f"Car with {self.wheels} wheels"


class Converter(Car):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)
  
  def take_off(Self):
    return "taking off"

  def __str__(self):
    return f"Car is not a big deal"

panda = Converter(color = "green", price = "$30")
print(panda.color)
print(panda.windows)
print(panda.time)
