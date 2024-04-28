class Animal:
  def speak(self):
    return "Animal makes a sound"

class Dog(Animal):
  def speak(self):
    return "woof!"

class Cat(Animal):
  def speak(self):
    return "meow!"

class Cow(Animal):
  pass

  def make_animal_speak(animal):
    print(animal.speak())


dog=Dog()
cat=Cat()
cow=Cow()

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(cow)

