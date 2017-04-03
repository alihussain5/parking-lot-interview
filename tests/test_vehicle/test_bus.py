from unittest import TestCase

from infrastructure.spot import SpotSize
from vehicle.motorcycle import Bus


class BusTest(TestCase):
    def setUp(self):
        super(BusTest, self).setUp()
        self.test_bus = Bus('test bus')

    def test_size(self):
        self.assertEqual(self.test_bus.get_size, SpotSize.LARGE)

    def test_name(self):
        self.assertEqual(self.test_bus.get_name, 'test bus')

    def test_spot_count(self):
        self.assertEqual(self.test_bus.get_spot_count, 5)
