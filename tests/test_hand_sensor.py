import unittest
import sys
sys.path.append('../service')
from service.hand_sensor import HandSensor

class TestHandSensor(unittest.TestCase):

    # def setUp(self):
    #     print("\nRunning setUp method...")
    #     self.hs1  = HandSensor([0.091, 0.165, 0.223, 0.318, 0.373, 0.429, 0.481, 0.559, 0.638, 0.734], 
    #                            [275, 272, 271, 268, 19, 265, 260, 261, 262, 260], 
    #                            [-100, 201, 202, 210, 222, 220, 199, -100, 195, 189])
    # def tearDown(self):
    #     print("Running tearDown method...")

    def test_interpolation(self):
        self.hs1  = HandSensor([0.091, 0.165, 0.223, 0.318, 0.373, 0.429, 0.481, 0.559, 0.638, 0.734], 
                        [275, 272, 271, 268, 19, 265, 260, 261, 262, 260], 
                        [-100, 201, 202, 210, 222, 220, 199, -100, 195, 189])
        res = self.hs1.interpolation([275, 272, 271, 268, 19, 265, 260, 261, 262, 260]) 
        self.assertEqual(res, [275, 272, 271, 268, 266, 265, 260, 261, 262, 260])

    def test_interpolation2(self):
        self.hs1  = HandSensor([0.091, 0.165, 0.223, 0.318, 0.373, 0.429, 0.481, 0.559, 0.638, 0.734], 
                        [275, 272, 271, 268, 19, 265, 260, 261, 262, 260], 
                        [-100, 201, 202, 210, 222, 220, 199, -100, 195, 189])
        res = self.hs1.interpolation([275, 272, 271, 268, 19, 265, 260, 261, 262, 260]) 
        self.assertEqual(res, [275, 272, 271, 268, 266, 265, 260, 261, 262, 260])


# if __name__ == "__main__":
#     unittest.main()

