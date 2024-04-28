class Animal:
  def __init__(self,name,colour):
    self.animal_name=name
    self.animal_colour=colour

  def Sound(self):
    print(f"{self.animal_name}is loud")

Dog=Animal("beagle","brown")
Cat=Animal("persian","white")

print(Dog.animal_name)
print(Dog.animal_colour)
print(Cat.animal_name)
print(Cat.animal_colour)
Dog.Sound()