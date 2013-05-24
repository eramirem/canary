import sys, signal

def trigger_alarm(signal, frame):
	raise SecurityError(408, 'REQUEST_TIMEOUT')

class Error(Exception):
    pass

class SecurityError(Error):
    def __init__(self, code, message):
        Error.__init__(self,message)
        self.code = code

class Security():
	def __init__(self, passcode=None, status=0, alarm=0):
		self.passcode = passcode
		self.status = status
		self.alarm = alarm
		self.sensors = {}

	def set_passcode(self, passcode=None):
		self.passcode = passcode
	
	def add_sensor(self, sensor=None):
		self.sensors.update(sensor)

	def set_status(self, status=0):
		self.status = status

	def get_status(self):
		return self.status

	def arm_home(self):
		try:
			self.enter_passcode()
			self.set_status(1)
		except:
			self.alarm = 1

	def arm_away(self):
		try:
			self.enter_passcode()
			self.set_status(2)
		except:
			self.alarm = 1

	def disarm(self):
		try:
			self.enter_passcode()
			self.set_status(0)
			self.alarm = 0
		except:
			self.alarm = 1

	def open_door(self, key):
		if key not in self.sensors:
			raise SecurityError(404, 'NOT_FOUND')
		if self.sensors[key]['class'] != 'door':
			raise SecurityError(404, 'NOT_FOUND')
		self.sensors[key]['status'] = 1
		if self.get_status() == 1:
			self.alarm = 1
		if self.get_status() == 2:
			self.disarm()


	def open_window(self, key):
		if key not in self.sensors:
			raise SecurityError(404, 'NOT_FOUND')
		if self.sensors[key]['class'] != 'window':
			raise SecurityError(404, 'NOT_A_FOUND')
		self.sensors[key]['status'] = 1
		if self.get_status() == 1:
			self.alarm = 1
		if self.get_status() == 2:
			self.disarm()

	def enter_passcode(self):
		signal.signal(signal.SIGALRM, trigger_alarm)
		signal.alarm(10)
		passcode = raw_input('enter passcode: ')
		while (int(passcode) != self.passcode):
			passcode = raw_input('enter passcode: ')
		signal.alarm(0)		
		