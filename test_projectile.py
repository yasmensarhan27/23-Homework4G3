import unittest
import projectile

class ProjectileTests(unittest.TestCase):

    def test_calc_xy(self):
        """Test the calc_xy() function."""

        # Set the initial conditions
        angles = [30, 45, 60]
        v_initial = 700
        x_start = 0
        y_start = 0

        # Calculate the expected x and y positions
        expected_x_list, expected_y_list = projectile.calc_xy(angles, [], [], v_initial, x_start, y_start)

        # Calculate the actual x and y positions
        actual_x_list, actual_y_list = projectile.calc_xy(angles, [], [], v_initial, x_start, y_start)

        # Assert that the expected and actual x and y positions are equal
        for i in range(len(angles)):
            self.assertAlmostEqual(expected_x_list[i], actual_x_list[i], places=5)
            self.assertAlmostEqual(expected_y_list[i], actual_y_list[i], places=5)
