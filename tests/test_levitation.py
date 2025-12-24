import sys
import os
import unittest

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from modules.levitation import LevitationController

class TestLevitation(unittest.TestCase):
    def test_initial_state(self):
        lev = LevitationController(target_gap=15.0)
        self.assertEqual(lev.target_gap, 15.0)
        self.assertFalse(lev.levitation_active)

    def test_pid_output(self):
        lev = LevitationController()
        lev.activate()
        # Mock gap = 8.0, Target = 10.0 -> Error = 2.0
        # Output should be roughly Kp * Error = 1.5 * 2 = 3.0 (ignoring I and D for first step)
        output = lev.update(current_gap_sensor_val=8.0, dt=0.1)
        self.assertGreater(output, 0, "PID output should be positive to lift the pod")

if __name__ == '__main__':
    unittest.main()
