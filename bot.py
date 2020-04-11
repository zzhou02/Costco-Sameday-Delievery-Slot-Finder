from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound
import random
import time


class Bot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url
        self.driver.get(url)

    def wait(self, element_xpath):
        wait = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, element_xpath)))

    def base(self):
        self.driver.get(self.url)

    def button(self, url_xpath):
        self.driver.find_element_by_xpath(url_xpath).click()

    def input(self, input_xpath, content):
        self.driver.find_element_by_xpath(input_xpath).send_keys(content)

    def makeSound(self):
        winsound.Beep(500, 5000)

    def findSingle(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def pause(self):
        time.sleep(30)
