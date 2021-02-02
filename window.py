
from selenium import webdriver as wd
import time

class Window :
    def __init__(self, path="C:/Users/muns3/Downloads/chromedriver_win32 (1)/chromedriver.exe") :
        self.wd_path = path

    def goToUrl(self, url) :
        self.driver = wd.Chrome(self.wd_path)
        self.driver.get(url)

        return self.driver

    def runScript(self, commands, delay=0) :
        result = []
        
        for command in commands :
            result.append(self.driver.execute_script(command))
            time.sleep(delay)

        return result