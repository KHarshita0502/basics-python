class Bike:
  pass

Duke=Bike()
Duke.name="RC390"
Duke.cc=390
print(Duke.cc)

RE=Bike()
RE.name="classic350"
RE.CC=350
print(RE.name)

from os import name
class Bike:
   def __init__(self,name,cc):
     self.bike_name=name
     self.bike_cc=cc

Duke=Bike("RC390",390)
RE=Bike("Classic350",350)

print(Duke.bike_name)
print(RE.bike_name)

