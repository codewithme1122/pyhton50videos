class Person:
  name = "ALI"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "maqsooda"
a.occupation = "principle of unique"

b.name = "kashan"
b.occupation = "a friend"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
