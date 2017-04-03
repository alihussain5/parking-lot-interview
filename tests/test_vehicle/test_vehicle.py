from unittest import TestCase

from infrastructure.spot import SpotSize
from vehicle.vehicle import Vehicle


class TestVehicle(Vehicle):
    def __init__(self):
        super(TestVehicle, self).__init__('test vehicle', SpotSize.LARGE)


class VehicleTest(TestCase):
    def test_get_name(self):
        test_vehicle = TestVehicle()

        self.assertEqual(test_vehicle.get_name, 'test vehicle')

    def test_get_size(self):
        test_vehicle = TestVehicle()

        self.assertEqual(test_vehicle.get_size, SpotSize.LARGE)
