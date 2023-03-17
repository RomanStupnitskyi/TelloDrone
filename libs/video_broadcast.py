import cv2
import threading


class Video_Broadcast:
	def __init__(self, drone):
		self.drone = drone
		self.WINDOW_NAME = "TelloDrone"


	def start_watching(self):
		self.drone.tello.streamon()
		setattr(self, "frame_reader", True)
		
		self.frame_update_thread = threading.Thread(target=self.update_frame)
		self.frame_update_thread.start()
		print("Video broadcast has started")


	def update_frame(self):
		while True:
			if not hasattr(self, "frame_reader"):
				cv2.destroyWindow(self.WINDOW_NAME)
				return
			img = self.drone.tello.get_frame_read().frame
			cv2.imshow(self.WINDOW_NAME, img)
			cv2.waitKey(1) & 0xFF


	def stop_watching(self):
		self.drone.tello.streamoff()
		delattr(self, "frame_reader")
		print("Video broadcast has ended")
