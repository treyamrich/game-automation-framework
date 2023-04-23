from util.input_handling.mouse_controller import MouseController
from util.input_handling.keyboard_controller import KeyboardController
from util.input_handling.logger import Logger
import win32gui
import win32con
import time

class VirtualInputHandler:
    """
    Class encapsulates the logic for virtual clicking and keyboard inputs
    """

    def __init__(self, script_name: str, log_serverity_level: str = 'warning'):
        """
        script_name: the name of the script folder under /scripts
        log_serverity_level: str specifies the logging level. All log msgs of the level and above will be logged.
        """
        self.image_dir = f'images\\{script_name}\\'
        self.logger = Logger(script_name, log_serverity_level)
        self.mouse = MouseController(self.logger)
        self.keyboard = KeyboardController(self.logger)
    
    def change_window(self, window_title: str):
        """
        Waits 1 second to change to the window.

        window_title: the name of the window to switch to
        """
        time.sleep(1)
        window = win32gui.FindWindow(None, window_title)
        # Switch to the window and maximize it
        if not window:
            self.logger.critical(f"Window not found {window_title}")
            exit(1)

        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)

    def random_click_position(self, position: tuple):
        """
        Uses a random click type to click a specific position.

        position: the (x, y) position of where to click
        """
        self.mouse.random_click_position(position)

    def click_image(self, image_name: str, resolution: float = 0.55) -> bool:
        """
        Clicks an image using a random click type and random position in the image.

        image_name: the image to locate inside the folder on the path images\script_name
        resolution: must be between 0 and 1; it's the threshold of what to consider a 'matched' image

        return: true if the image was found and clicked, false otherwise
        """
        return self.mouse.click_image(self.image_dir + image_name, resolution)
    
    def wait_for_image(self, image_name: str, duration: float = float('inf'), resolution: float = 0.55) -> bool:
        """
        Waits for an image to appear and clicks on it. The initial minimum wait time is 1 second.

        image_name: the image to locate inside the folder on the path images\script_name
        duration: max amount of seconds to wait for the image. Waits forever if not specified.
        resolution: must be between 0 and 1; it's the threshold of what to consider a 'matched' image

        return: true if the image was found and clicked, false otherwise
        """
        return self.mouse.wait_for_image(self.image_dir + image_name, duration, resolution)