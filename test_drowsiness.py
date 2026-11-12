import unittest
from drowsiness import eye_aspect_ratio,analyze
class DrowsinessTests(unittest.TestCase):
 def test_open_eye_ratio(self): self.assertAlmostEqual(eye_aspect_ratio([(0,1),(1,0),(2,0),(4,1),(2,2),(1,2)]),.5)
 def test_sustained_closure_triggers_signal(self):
  eye=[(0,0),(1,0),(2,0),(4,0),(2,0),(1,0)]; shut=[(0,0),(1,0),(2,0),(4,0),(2,0),(1,0)]; s=[{"time":0,"left_eye":[(0,0),(1,1),(2,1),(4,0),(2,-1),(1,-1)],"right_eye":[(0,0),(1,1),(2,1),(4,0),(2,-1),(1,-1)]},{"time":.5,"left_eye":shut,"right_eye":shut},{"time":2,"left_eye":shut,"right_eye":shut},{"time":2.2,"left_eye":[(0,0),(1,1),(2,1),(4,0),(2,-1),(1,-1)],"right_eye":[(0,0),(1,1),(2,1),(4,0),(2,-1),(1,-1)]}]
  self.assertEqual(len(analyze(s,.22,1)),1)
if __name__=="__main__":unittest.main()
