# TelloDrone
**TelloDrone is a Python-based project that allows users to control a DJI Tello drone through their computer keyboard. The project uses object-oriented programming (OOP) and integrates the DJI Tello API, OpenCV, and threading for controlling and broadcasting video from the drone.**

# Installation
The TelloDrone project can be installed by cloning the project from its GitHub repository and installing the required dependencies listed in the `requirements.txt` file.

# Usage
To use the TelloDrone project, simply run the main.py script, which will connect to the drone and start the video feed. The user can then use their keyboard to control the drone's movements, perform flips, and land the drone.
- `git clone https://github.com/RomanStupnitskyi/TelloDrone.git`
- `pip install -r requirements.txt`
- `python3 main.py`

# Project Structure
**The TelloDrone project has the following structure:**  

```
TelloDrone/
├── libs/
│   ├── __init__.py
│   ├── controller.py
│   ├── drone.py
│   └── video_broadcast.py
├── main.py
└── README.md
```

- `main.py`: the main script that connects to the drone and starts the controller and video broadcast threads.
- `drone.py`: defines the TelloDrone class that contains methods for controlling the drone.
- `controller.py`: defines the Controller class that reads user keyboard inputs and translates them into drone commands.
- `video_broadcast.py`: defines the Video_Broadcast class that starts and stops the drone's video stream and updates the video frames in a separate thread.
- `__init__.py`: initializes the TelloDrone class.

# TelloDrone Class
The `TelloDrone` class is the main class of the TelloDrone project and contains the following methods:

- `run()`: connects to the drone, starts the video feed, and reads user input from the keyboard.
- `takeoff()`: tells the drone to take off and prints a message.
- `takeoff_watching()`: starts or stops watching the video feed, depending on whether the feed is currently being watched.
- `move_by_velocity(velocity)`: moves the drone in the specified velocity and direction.
- `flip(direction)`: performs a flip in the specified direction and prints a message.
- `land()`: tells the drone to land and prints a message.
- `quite()`: lands the drone, stops the video feed, and prints a completion message before ending the program.

# Controller Class
The `Controller` class reads the user input from the keyboard and translates it into drone commands. It has the following methods:

- `read_input()`: continuously reads user input from the keyboard and translates it into drone commands until the user presses the "q" key to quit the program.
- `check_commands()`: checks the user's input and executes the appropriate command.
- `check_commands_loop()`: runs continuously in a separate thread, calling `check_commands()` on each keyboard input.

# Video_Broadcast Class
The `Video_Broadcast` class starts and stops the drone's video stream and updates the video frames in a separate thread. It has the following methods:

- `start_watching()`: starts the video stream and updates the frames in a separate thread.
- `update_frame()`: continuously updates the video frames until the video stream is stopped.
- `stop_watching()`: stops the video stream and updates the frames.
