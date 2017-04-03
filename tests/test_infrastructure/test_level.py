from unittest import TestCase

from infrastructure.level import Level
from infrastructure.spot import SpotSize
from vehicle.bus import Bus
from vehicle.car import Car
from vehicle.motorcycle import Motorcycle
from vehicle.vehicle import Vehicle


class TestLargeVehicle(Vehicle):
    def __init__(self):
        super(TestLargeVehicle, self).__init__(
            'test large vehicle', SpotSize.LARGE)


class LevelTest(TestCase):
    def test_park_full(self):
        new_level = Level('tests/test_non_consecutive.txt')

        while 1:
            key = new_level.park(Motorcycle('test mc'))

            if not key:
                break

        key = new_level.park(Car('test car'))

        self.assertIsNone(key)

    def test_park_no_bigger_available(self):
        new_level = Level('tests/test_non_consecutive.txt')

        while 1:
            key = new_level.park(Car('test car'))

            if not key:
                break

        mc_spot_count = 0

        while 1:
            key = new_level.park(Motorcycle('test mc'))

            if not key:
                break

            mc_spot_count += 1

        self.assertEqual(mc_spot_count, 3)

    def test_proper_spot_count(self):
        new_level = Level('tests/test_non_consecutive.txt')

        large_spot_count, compact_spot_count, mc_spot_count = 0, 0, 0

        while 1:
            key = new_level.park(TestLargeVehicle())

            if not key:
                break

            large_spot_count += 1

        while 1:
            key = new_level.park(Car('test car'))

            if not key:
                break

            compact_spot_count += 1

        while 1:
            key = new_level.park(Motorcycle('test mc'))

            if not key:
                break

            mc_spot_count += 1

        self.assertEqual(large_spot_count, 16)
        self.assertEqual(compact_spot_count, 13)
        self.assertEqual(mc_spot_count, 3)

    def test_park_bus_no_space(self):
        new_level = Level('tests/test_non_consecutive.txt')

        key = new_level.park(Bus('test bus'))

        self.assertIsNone(key)

    def test_park_bus(self):
        new_level = Level('tests/test_consecutive.txt')

        bus_count = 0
        while 1:
            key = new_level.park(Bus('test bus'))

            if key is None:
                break
            bus_count += 1

        self.assertEqual(bus_count, 5)

    def test_park_bus_spots_left(self):
        new_level = Level('tests/test_consecutive.txt')

        while 1:
            key = new_level.park(Bus('test bus'))

            if key is None:
                break

        large_spot_count = 0

        while 1:
            key = new_level.park(TestLargeVehicle())

            if key is None:
                break

            large_spot_count += 1

        self.assertEqual(large_spot_count, 4)

    def test_unpark_empty(self):
        new_level = Level('tests/test_consecutive.txt')

        vehicle = new_level.unpark('test')

        self.assertIsNone(vehicle)

    def test_unpark_wrong_key(self):
        new_level = Level('tests/test_consecutive.txt')
        new_level.park(Car('test car'))

        vehicle = new_level.unpark('not the right key')
        self.assertIsNone(vehicle)

    def test_unpark_single(self):
        new_level = Level('tests/test_consecutive.txt')

        test_car = Car('test car')
        key = new_level.park(test_car)

        vehicle = new_level.unpark(key)

        self.assertIs(vehicle, test_car)

    def test_unpark_multiple(self):
        new_level = Level('tests/test_consecutive.txt')

        test_cars = [Car('test car') for i in xrange(5)]
        keys = [new_level.park(car) for car in test_cars]

        vehicles = [new_level.unpark(key) for key in keys]

        self.assertListEqual(test_cars, vehicles)

    def test_unpark_bus(self):
        new_level = Level('tests/test_consecutive.txt')

        for i in xrange(5):
            bus_key = new_level.park(Bus('test bus'))

        while 1:
            key = new_level.park(TestLargeVehicle())

            if key is None:
                break

        self.assertIsNone(new_level.park(Bus('test bus')))

        new_level.unpark(bus_key)

        large_count = 0

        while 1:
            key = new_level.park(TestLargeVehicle())

            if key is None:
                break

            large_count += 1

        self.assertEqual(large_count, 5)

    def test_park_in_unparked_spot(self):
        new_level = Level('tests/test_consecutive.txt')

        for i in xrange(45):
            car_key = new_level.park(Car('test car'))

        while 1:
            key = new_level.park(Motorcycle('test mc'))

            if not key:
                break

        self.assertIsNone(new_level.park(Motorcycle('test mc')))

        new_level.unpark(car_key)
        self.assertIsNotNone(new_level.park(Motorcycle('test mc')))
