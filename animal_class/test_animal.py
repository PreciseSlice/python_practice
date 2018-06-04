import unittest
import animal_class

animal = animal_class.Animal('Tim', 12)

class TestAnimalMethods(unittest.TestCase):

  def test_member_var(self):
    self.assertEqual(animal.is_alive, True)
    self.assertEqual(animal.health, "good")

  def test_init(self):
    self.assertEqual(animal.name, 'Tim')
    self.assertEqual(animal.age, 12)

unittest.main()