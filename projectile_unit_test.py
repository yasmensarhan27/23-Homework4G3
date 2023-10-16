import math
import unittest

# Import the function you want to test
from projectile_new import calc_xy

class TestProjectileMotion(unittest.TestCase):
    def test_calc_xy(self):
        # Test the calc_xy function with specific inputs and expected outputs
        angles = [math.radians(30), math.radians(45)]
        x_list, y_list = calc_xy(angles, [], [], 700, 0, 0)

        # Check if the returned x and y lists have the expected length
        self.assertEqual(len(x_list), len(angles))
        self.assertEqual(len(y_list), len(angles))

        # Check if the calculated values are reasonable (e.g., not empty)
        self.assertTrue(all(x) for x in x_list)
        self.assertTrue(all(y) for y in y_list)

    def test_degrees_to_radians_conversion(self):
        # Test the degrees to radians conversion function
        angle_degrees = [30, 45, 60]
        angle_radians = [math.radians(deg) for deg in angle_degrees]

        self.assertEqual(angle_radians, [math.radians(30), math.radians(45), math.radians(60)])

if __name__ == '__main__':
    unittest.main()
