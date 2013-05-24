import unittest
import canary
import time
from canary import SecurityError

class SecurityTestCase(unittest.TestCase):
	def setUp(self):
		self.security = canary.Security()
		self.security.add_sensor({'d1': {'class': 'door', 'status': 0}})
		self.security.add_sensor({'w1': {'class': 'window', 'status': 0}})
		self.security.set_passcode(1234)
	
	def test_arm_home(self):
		print 'Test Case 1'
		self.security.arm_home()
		self.assertEqual(self.security.status, 1)

		with self.assertRaises(canary.SecurityError):
			self.security.open_window('fizzbuzz')

		self.security.open_window('w1')
		self.assertEqual(self.security.alarm, 1)
		
		self.security.disarm()
		self.assertEqual(self.security.status, 0)
		self.assertEqual(self.security.alarm, 0)

	def test_arm_away(self):
		print 'Test Case 2'
		self.security.arm_away()

		self.security.open_door('d1')
		self.assertEqual(self.security.status, 0)
		self.assertEqual(self.security.alarm, 0)

	def test_alarm(self):
		print 'Test Case 3'
		self.security.arm_away()
		
		self.security.open_door('d1')
		self.assertEqual(self.security.alarm, 1)

		self.security.disarm()
		self.assertEqual(self.security.status, 0)
		self.assertEqual(self.security.alarm, 0)	

if __name__ == '__main__':
	output_file = 'output.txt'
   	f = open(output_file, "w")
   	runner = unittest.TextTestRunner(f)
   	unittest.main(testRunner=runner)
   	f.close()