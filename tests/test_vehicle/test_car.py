from unittest import TestCase

from infrastructure.spot import SpotSize
from vehicle.car import Car


class CarTest(TestCase):
    def setUp(self):
        super(CarTest, self).setUp()
        self.test_car = Car('test car')

    def test_size(self):
        self.assertEqual(self.test_car.get_size, SpotSize.COMPACT)

    def test_name(self):
        self.assertEqual(self.test_car.get_name, 'test car')
