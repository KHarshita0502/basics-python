class Location:
  def _init_(self,l1,l2):
    self.l1=l1
    self.l2=l2

  def _add_(self,other):
    print(f"{self.l1+other.l1}+{self.l2+other.l2}")

