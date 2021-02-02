
from window import Window
from command import JavascriptCommand as jc
import pyautogui as pg
import time

class AutoViews :
    def __init__(self) :
        self.window = Window()

    def __checkAds(self) :
        skip_button = self.window.runScript([jc.checkSkipButton()])[0]
        skip_button2 = self.window.runScript([jc.checkSkipButton2()])[0]

        if skip_button or skip_button2 :
            return True

        else :
            return False

    def __skipSecond(self, delay=0) :
        video_length = int(self.window.runScript([jc.getVideoLength()])[0])
        skip_now = 0

        pg.press("space")

        while skip_now < video_length :
            if self.__checkAds() :
                try :
                    self.window.runScript([jc.clickSkipButton()])

                except :
                    pass

            else :
                video_length = int(self.window.runScript([jc.getVideoLength()])[0])
                pg.press("right")
                skip_now += 5

            print("length : ", skip_now)
            time.sleep(delay)

    def playVideo(self, url, skip_delay=0.1, delay=5) :
        self.driver = self.window.goToUrl(url)
        time.sleep(delay)

        self.__skipSecond(delay=skip_delay)
        self.driver.close()




