class Cake:
    eggs = 4
    sugar = 300 
    milk = 200
    butter = 50
    flour = 250
    baking_soda = 20
    vanilla = 10

    topping = None
    garnish = None

    is_baked = False

    def __init__(self, topping="no topping", garnish="no garnish"):
      self.topping = topping
      self.garnish = garnish 

    def bake(self):
      self.is_baked = True

    def cake_is_ready(self):
      return self.is_baked

mint_Cake = Cake(topping='Mint', garnish='cookie')
mint_Cake.bake()
cake_is_done = mint_Cake.cake_is_ready()

print(cake_is_done)
