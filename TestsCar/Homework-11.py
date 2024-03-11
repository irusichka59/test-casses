import unittest
from car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Camry", miles_limit=100)

    def test_start_engine(self):
        self.assertEqual(self.car.start_engine(), "Engine started.")
        self.assertTrue(self.car._Car__is_engine_started)

    def test_drive_within_limit(self):
        self.car.start_engine()
        self.assertEqual(self.car.drive(50), "Driving 50 miles.")
        self.assertEqual(self.car.miles_limit, 50)

    def test_drive_engine_off_within_limit(self):
        self.assertEqual(self.car.drive(50), "Cannot drive. Engine is off.")

    def test_drive_engine_off_exceed_limit(self):
        self.assertEqual(self.car.drive(150), "Cannot drive. Engine is off.")

    def test_drive_after_engine_stopped(self):
        self.car.start_engine()
        self.car.stop_engine()
        self.assertEqual(self.car.drive(50), "Cannot drive. Engine is off.")

    def test_multiple_drives_within_limit(self):
        self.car.start_engine()
        self.car.drive(20)
        self.car.drive(30)
        self.assertEqual(self.car.miles_limit, 50)

    def test_multiple_engine_starts(self):
        self.car.start_engine()
        self.car.start_engine()
        self.assertTrue(self.car._Car__is_engine_started)

    def test_multiple_engine_stops(self):
        self.car.start_engine()
        self.car.stop_engine()
        self.car.stop_engine()
        self.assertFalse(self.car._Car__is_engine_started)

    def test_multiple_engine_starts_stops(self):
        self.car.start_engine()
        self.car.stop_engine()
        self.car.start_engine()
        self.car.stop_engine()
        self.assertFalse(self.car._Car__is_engine_started)

    def test_drive_zero_miles(self):
        self.car.start_engine()
        self.assertEqual(self.car.drive(0), "Driving 0 miles.")
        self.assertEqual(self.car.miles_limit, 100)


if __name__ == '__main__':
    unittest.main()
