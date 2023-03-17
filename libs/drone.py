from djitellopy import Tello
from .controller import Controller
from .video_broadcast import Video_Broadcast
import sys


class TelloDrone:
	def __init__(self):
		self.tello = Tello()
		
		self.controller = Controller(self)
		self.video_broadcast = Video_Broadcast(self)
		self.DIRECTIONS = {
				"l": "left",
				"r": "right",
				"f": "forward",
				"b": "back",
		}


	def run(self):
		self.tello.connect()
		print("Drone is connected")
		self.video_broadcast.start_watching()
		self.controller.read_input()


	def takeoff(self):
		self.tello.takeoff()
		print("Takeoff drone")


	def takeoff_watching(self):
		if not hasattr(self.video_broadcast, "frame_reader"):
			self.video_broadcast.start_watching()
		else:
			self.video_broadcast.stop_watching()


	def move_by_velocity(self, velocity: object):
		self.tello.send_rc_control(
			*velocity.values()
		)


	def flip(self, direction: str):
		self.tello.flip(direction)
		print(f"Drone did a {self.DIRECTIONS[direction]} flip")


	def land(self):
		self.tello.land()
		print("Drone has landed")


	def quite(self):
		self.land()
		if hasattr(self.video_broadcast, "frame_reader"):
			self.video_broadcast.stop_watching()
		print("Drone operation is completed")
		self.tello.end()
		sys.exit(0)
