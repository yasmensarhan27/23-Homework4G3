#import the necessary libraries to run the code
import math
import unittest
# Import the function you want to test from the module you created
from projectile_new import calc_xy
#create a class for the unittisting including 2 functions
class TestProjectileMotion(unittest.TestCase):
        """A class to Unittesting."""
#function to test the calculation
    def test_calc_xy(self):
            """A function that Test the calc_xy function with specific inputs and expected outputs. """
        angles = [round((math.radians(60)),1), round((math.radians(75)),1)]
        x_list, y_list = calc_xy(angles, [], [], 700, 0, 0)
        #------------
        # Check if the returned x and y lists have the expected length
        self.assertEqual(len(x_list), len(angles))
        self.assertEqual(len(y_list), len(angles))
        # Check if the calculated values are reasonable (e.g., not empty)
        self.assertTrue(all(x > 0 for x in x_list))
        self.assertTrue(all(y < 0 for y in y_list))
        #--------------
    #functuon to test the conversion
    def test_degrees_to_radians_conversion(self):
                """A function that Test the degrees to radians conversion function """
        angle_degrees = [60, 75, 90]
        angle_radians = [round(math.radians(deg),1) for deg in angle_degrees]
        for i in range(angle_radians):
            for i in range(angle_degrees):
                assert angle_radians[i] == angle_degrees[i]
#----------
if __name__ == '__main__':
    unittest.main()
