from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound
import time
import sys


class Bot:
    def __init__(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.url = url
            self.driver.maximize_window()
            self.driver.get(url)
        except:
            sys.exit()

    def wait(self, element_xpath):
        wait = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, element_xpath)))

    def base(self):
        self.driver.get(self.url)

    def makeSound(self):
        winsound.Beep(500, 5000)

    def findSingle(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def pause(self):
        time.sleep(30)
