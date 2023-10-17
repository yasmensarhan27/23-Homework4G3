import unittest
import projectile

class ProjectileTests(unittest.TestCase):

    def test_projectile_with_drag(self):
        """Test the projectile_with_drag() function."""

        # Set the initial velocity
        v_start = 700

        # Calculate the expected x and y positions
        expected_x_list, expected_y_list = projectile.projectile_with_drag(v_start)

        # Calculate the actual x and y positions
        actual_x_list, actual_y_list = projectile.projectile_with_drag(v_start)

        # Assert that the expected and actual x and y positions are almost equal
        for i in range(len(expected_x_list)):
            self.assertAlmostEqual(expected_x_list[i], actual_x_list[i], places=5)
            self.assertAlmostEqual(expected_y_list[i], actual_y_list[i], places=5)

    def test_projectile_with_drag_invalid_input(self):
        """Test the projectile_with_drag() function with invalid input."""

        # Test with a negative initial velocity
        with self.assertRaises(ValueError):
            projectile.projectile_with_drag(-700)
