from unittest import TestCase

from infrastructure.spot import Spot, SpotSize
from vehicle.bus import Bus
from vehicle.car import Car
from vehicle.motorcycle import Motorcycle


class SpotTest(TestCase):
    def test_is_empty(self):
        new_spot = Spot(SpotSize.LARGE)
        self.assertTrue(new_spot.is_empty())

        new_spot.park(Car('test'))
        self.assertFalse(new_spot.is_empty())

        new_spot.unpark()
        self.assertTrue(new_spot.is_empty())

    def test_get_size(self):
        large_spot = Spot(SpotSize.LARGE)
        compact_spot = Spot(SpotSize.COMPACT)
        mc_spot = Spot(SpotSize.MOTORCYCLE)

        self.assertEqual(large_spot.get_size, SpotSize.LARGE)
        self.assertEqual(compact_spot.get_size, SpotSize.COMPACT)
        self.assertEqual(mc_spot.get_size, SpotSize.MOTORCYCLE)

    def test_can_fit_empty(self):
        large_spot = Spot(SpotSize.LARGE)
        compact_spot = Spot(SpotSize.COMPACT)
        mc_spot = Spot(SpotSize.MOTORCYCLE)

        self.assertTrue(large_spot.can_fit(Bus('test bus')))
        self.assertFalse(compact_spot.can_fit(Bus('test bus')))
        self.assertFalse(mc_spot.can_fit(Bus('test bus')))

        self.assertTrue(large_spot.can_fit(Car('test car')))
        self.assertTrue(compact_spot.can_fit(Car('test car')))
        self.assertFalse(mc_spot.can_fit(Car('test car')))

        self.assertTrue(large_spot.can_fit(Motorcycle('test mc')))
        self.assertTrue(compact_spot.can_fit(Motorcycle('test mc')))
        self.assertTrue(mc_spot.can_fit(Motorcycle('test mc')))

    def test_can_fit_non_empty(self):
        spot = Spot(SpotSize.LARGE)
        spot.park(Car('test'))

        self.assertFalse(spot.can_fit(Car('test')))

    def test_park_can_fit(self):
        test_spot = Spot(SpotSize.LARGE)
        test_car = Car('test car')

        self.assertTrue(test_spot.park(test_car))

    def test_park_non_empty(self):
        test_spot = Spot(SpotSize.LARGE)
        test_spot.park(Car('test car'))

        self.assertFalse(test_spot.park(Car('test car')))

    def test_park_wrong_size(self):
        test_spot = Spot(SpotSize.MOTORCYCLE)
        self.assertFalse(test_spot.park(Car('test car')))

    def test_unpark_no_vehicle(self):
        test_spot = Spot(SpotSize.LARGE)
        self.assertIsNone(test_spot.unpark())

    def test_unpark(self):
        test_spot = Spot(SpotSize.LARGE)
        test_car = Car('test car')
        test_spot.park(test_car)

        test_car_unparked = test_spot.unpark()

        self.assertEqual(test_car_unparked, test_car)
