from unittest import TestCase

from infrastructure.spot import SpotSize
from vehicle.motorcycle import Motorcycle


class MotorcycleTest(TestCase):
    def setUp(self):
        super(MotorcycleTest, self).setUp()
        self.test_mc = Motorcycle('test mc')

    def test_size(self):
        self.assertEqual(self.test_mc.get_size, SpotSize.MOTORCYCLE)

    def test_name(self):
        self.assertEqual(self.test_mc.get_name, 'test mc')
