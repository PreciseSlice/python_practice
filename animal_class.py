# class Animal(object):
#     def __init__(self, name):
#         self.name = name


# zebra = Animal("Jeffrey")

# print(zebra.name)


# class Animal(object):

#     def __init__(self, name, age, is_hungry):
#         self.name = name
#         self.age = age
#         self.is_hungry = is_hungry


# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)


# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)


# # Member variable globaly scoped
# class Animal(object):
#     # Member variable
#     is_alive = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)

# print (zebra.name, zebra.age, zebra.is_alive)
# print (giraffe.name, giraffe.age, giraffe.is_alive)
# print (panda.name, panda.age, panda.is_alive)


# class Animal(object):

#   is_alive = True
  
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age


#   def description(self):
#     print (self.name)
#     print (self.age)
    
# hippo = Animal("Bob", 3)
# hippo.description()


class Animal(object):

  is_alive = True
  health = "good"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def description(self):
    print (self.name)
    print (self.age)
    
hippo = Animal("Bob", 3)
hippo.description()

sloth = Animal("Tim", 2)
ocelot = Animal("Marb", 4)

print(hippo.health)
print(sloth.health)
print(ocelot.health)

