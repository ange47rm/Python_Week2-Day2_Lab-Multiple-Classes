import unittest
from src.person import Person
from src.bus import Bus

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, "Sun")

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)


    # @unittest.skip("Delete this line to run the test")
    def test_person_gets_on_bus(self):
        person1 = Person("Skye", 33, "SilverLane")
        person2 = Person("David", 86, "GreenTown")
        bus = Bus(88, "SilverLane")
        self.assertEqual(True, person1.person_gets_on_bus(bus))
        #self.assertEqual(False, person2.person_gets_on_bus(bus))
