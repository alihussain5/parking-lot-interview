import mock
from unittest import TestCase

from infrastructure.garage import Garage
from vehicle.car import Car


class GarageTest(TestCase):
    def setUp(self):
        super(GarageTest, self).setUp()

        self.test_garage = Garage(4)
        self.test_car = Car('Test Car')

    @mock.patch('infrastructure.garage.Level.park', return_value='test')
    def test_park(self, level_park):
        key = self.test_garage.park(self.test_car)

        self.assertEqual(level_park.call_args[0][0], self.test_car)
        self.assertEqual(level_park.call_count, 1)
        self.assertEqual(key, 'test')

    @mock.patch('infrastructure.garage.Level.park', return_value=None)
    def test_park_none(self, level_park):
        key = self.test_garage.park(self.test_car)

        self.assertIsNone(key)
        self.assertEqual(level_park.call_count, 4)

    @mock.patch('infrastructure.garage.Level.park', return_value='test')
    @mock.patch('infrastructure.garage.Level.unpark')
    def test_unpark(self, level_unpark, level_park):
        level_unpark.return_value = self.test_car

        key = self.test_garage.park(self.test_car)
        vehicle = self.test_garage.unpark(key)

        self.assertEqual(vehicle, self.test_car)
        self.assertEqual(level_unpark.call_count, 1)
        self.assertEqual(level_unpark.call_args[0][0], 'test')

    @mock.patch('infrastructure.garage.Level.unpark', return_value=None)
    def test_unpark_none(self, level_unpark):
        vehicle = self.test_garage.unpark('test')

        self.assertIsNone(vehicle)
        self.assertEqual(level_unpark.call_count, 0)
