class Party:
  def _init_(self,name,money):
    self.name=name
    self.money=money

  def _gt_(self,other):
    if self.money>other.money:
      return True
    else:
      return False

p1=Party("syeda",3000)
p2=Party("nafisa",4000)
if p1>p2:
  print(f"{p1.name} will pay the money")
else:
  print(f"{p2.name} will pay the mmoney")
