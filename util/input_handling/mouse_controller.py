import pyautogui
import time
import random

class MouseController:
    def __init__(self, logger):
        self.logger = logger

    def _log_mouse_event(self, click_type, position=None, duration=None):
        msg = f"Click Action: {click_type}"
        if position:
            msg += f' {str(position)}'
        if duration:
            msg += f' {str(duration)}s'
        self.logger.debug(msg)

    def _random_point_within_rect(self, rect_corners: list) -> tuple:
        """
        rect: the coordinates of the recangle in the order top left, top right, bottom right and bottom left

        return: a random point within the rectangle
        """
        # Define the corners of the rectangle
        top_left, top_right, bottom_right, bottom_left = rect_corners

        # Get the x and y limits of the rectangle
        x_min, y_min = top_left
        x_max, y_max = bottom_right

        # Generate random coordinates within the rectangle
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        return (x, y)
    
    def _get_img_corner_coords(self, image_path: str, resolution: float) -> list:
        """
        image_path: the image to locate
        resolution: must be between 0 and 1; it's the threshold of what to consider a 'matched' image

        return: a list containing the four coordinates
        """
        try:
            img_location_obj = pyautogui.locateOnScreen(image_path, confidence=resolution)
        except IOError:
            self.logger.critical(f'Path to image does not exist {image_path}')
            exit(1)

        corners_coordinates = []
        if img_location_obj:
            left, top = img_location_obj.left, img_location_obj.top
            right = img_location_obj.left + img_location_obj.width
            bottom = img_location_obj.top + img_location_obj.height
            corners_coordinates.append((left, top))
            corners_coordinates.append((right, top))
            corners_coordinates.append((right, bottom))
            corners_coordinates.append((left, bottom))
        else:
            self.logger.warning(f"Image was not located: {image_path}")
        return corners_coordinates
    
    def _get_img_box_coords(self, image_path: str, resolution: float):
        return pyautogui.locateOnScreen(image_path, confidence=resolution)
    
    def _tap(self, position: tuple):
        rand_duration = random.uniform(0.2,0.6)
        # Move the mouse to the starting position of the object to be dragged
        pyautogui.moveTo(position, duration = rand_duration)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        self._log_mouse_event("Tap", position, rand_duration)

    def _drag_click(self, position: tuple):
        xTranslate = random.randint(-15,15)
        yTranslate = random.randint(-15,15)
        new_x, new_y = position[0]+xTranslate, position[1]+yTranslate
        rand_duration = random.uniform(0.1,0.4)
        pyautogui.moveTo(new_x, new_y)
        pyautogui.mouseDown()
        pyautogui.dragTo(position, duration=rand_duration)
        pyautogui.mouseUp()
        self._log_mouse_event("Drag Click", position, rand_duration)

    def _drag_click_2(self, position: tuple):
        xTranslate = random.randint(-15,15)
        yTranslate = random.randint(-15,15)
        xTranslate2 = random.randint(-10,10)
        yTranslate2 = random.randint(-10,10)
        rand_duration = random.uniform(0.1,0.3)
        pyautogui.moveTo(position[0]+xTranslate, position[1]+yTranslate)
        pyautogui.mouseDown()
        pyautogui.dragTo(position, duration=rand_duration)
        rand_duration = random.uniform(0.1,0.3)
        pyautogui.moveTo(position[0]+xTranslate2, position[1]+yTranslate2)
        pyautogui.dragTo(position, duration=rand_duration)
        pyautogui.mouseUp()
        self._log_mouse_event("Drag Click 2", position, rand_duration)

    def _hold_click(self, position: tuple):
        rand_duration = random.uniform(0.2,0.6)
        pyautogui.moveTo(position, duration= rand_duration)
        pyautogui.mouseDown()
        time.sleep(rand_duration)
        pyautogui.mouseUp()
        self._log_mouse_event("Hold Click", position, rand_duration)

    def random_click_position(self, position: tuple):
        """
        Uses a random click type to click a specific position.

        position: the (x, y) position of where to click
        """
        click_types = [self._tap, self._drag_click, self._drag_click_2, self._hold_click]
        click = random.choice(click_types)
        click(position)

    def click_image(self, image_path: str, resolution: float) -> bool:
        """
        Clicks an image using a random click type and random position in the image.

        image_path: the image to locate
        resolution: must be between 0 and 1; it's the threshold of what to consider a 'matched' image

        return: true if the image was found and clicked, false otherwise
        """
        img_coords = self._get_img_corner_coords(image_path, resolution)
        if not img_coords: return False
        point_in_image = self._random_point_within_rect(img_coords)
        self._log_mouse_event("Click Image")
        self.random_click_position(point_in_image)
        return True

    def wait_for_image(self, image_path: str, duration: float, resolution: float) -> bool:
        """
        Waits for an image to appear and clicks on it. The initial minimum wait time is 1 second.

        image_path: the image to locate
        duration: max amount of seconds to wait for the image. Waits forever if not specified.
        resolution: must be between 0 and 1; it's the threshold of what to consider a 'matched' image

        return: true if the image was found and clicked, false otherwise
        """
        self._log_mouse_event("Wait for image")
        while duration > 0:
            time.sleep(1)
            #If image is found
            if self.click_image(image_path, resolution):
                return True
            duration -= 1
        return False