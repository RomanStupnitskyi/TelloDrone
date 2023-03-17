import threading
import keyboard
from time import sleep


class Controller:
	def __init__(self, drone):
		self.drone = drone
		self.default_velocity = {'x': 0, 'y': 0, 'z': 0, 'r': 0}

		self.MOVE_COMMAND = "move_by_velocity"
		self.COMMAND_TIMEOUT = 2
		self.MOVE_TIMEOUT = 0.05

		self.VELOCITY = 50
		self.MAX_VELOCITY = 100
		self.MIN_VELOCITY = -100

		self.commands = {
				# Normally commands
				"normally": {
					"b": ("show_battery", []),
					"e": ("takeoff", []),
					"v": ("takeoff_watching", []),
					"l": ("land", []),
					"q": ("quite", []),
					"f+left": ("flip", ["l"]),
					"f+right": ("flip", ["r"]),
					"f+up": ("flip", ["f"]),
					"f+down": ("flip", ["b"]),
				},
				# Move commands
				"move": {
					"x": {
						'd': self.VELOCITY,
						'a': -self.VELOCITY,
					},
					"y": {
						'w': self.VELOCITY,
						's': -self.VELOCITY,
					},
					"z": {
						'up': self.VELOCITY,
						'down': -self.VELOCITY,
					},
					"r": {
						'right': self.VELOCITY,
						'left': -self.VELOCITY,
					},
				}
		}


	def read_input(self):
		self.read_input_device_thread = threading.Thread(target=self.check_commands_loop)
		self.read_input_device_thread.start()


	def check_commands(self) -> bool:
		cmd, args, timeout = None, None, 0

		# check normally commands
		for key, (command, arguments) in self.commands["normally"].items():
			if "+" in key:
				is_pressed = all(keyboard.is_pressed(k) for k in key.split("+"))
				if is_pressed:
					cmd, args, timeout = command, arguments, self.COMMAND_TIMEOUT
					break
			elif keyboard.is_pressed(key):
				cmd, args, timeout = command, arguments, self.COMMAND_TIMEOUT
				break

		# check move keys
		active_move_axis = list(
			filter(
				lambda axis: any(keyboard.is_pressed(k) for k in self.commands["move"][axis].keys()),
	  			self.commands["move"].keys()
			)
		)
		velocity = self.default_velocity.copy()
		
		for axis in active_move_axis:
			axis_velocity = self.commands["move"][axis]
			active_keys = list(filter(lambda key: keyboard.is_pressed(key), axis_velocity.keys()))
			for active_key in active_keys:
				value = axis_velocity[active_key]
				velocity[axis] = max(min(value, self.MAX_VELOCITY), self.MIN_VELOCITY)
		
		if not cmd:
			cmd, args, timeout = self.MOVE_COMMAND, [velocity], self.MOVE_TIMEOUT
		
		try:
			command = getattr(self.drone, cmd)
			command(*args)
			sleep(timeout)
		except Exception as error:
			print(error)


	def check_commands_loop(self):
		while True:
			if not self.drone:
				print("end")
				return
			self.check_commands()
	