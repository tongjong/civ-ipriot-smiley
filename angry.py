from smiley import Smiley
from blinkable import Blinkable
import time

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [59, 60, 50, 53, 42, 45, 35, 36]
        for pixel in mouth:
            self.pixels[pixel] = self.BLACK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [17, 18, 21, 22]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLACK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=0.05):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()