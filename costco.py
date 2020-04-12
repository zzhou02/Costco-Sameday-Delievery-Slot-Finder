from selenium import webdriver
from bot import Bot
import sys
import winsound
import time

baseUrl = "https://sameday.costco.com/store/checkout_v3"
after_login_delivery_time_xpath = '//*[@id="header"]/div/div/div[5]/div[2]/span/a'
checkout_page_body_xpath = '//*[@id="store"]'
unavailable_xpath = '//*[@id="react-views-container"]/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/h1'


def main():
    while True:
        robot.base()
        robot.pause()
        # if the sorry message is not found we know that a delivery slot is found
        try:
            pageLoaded = robot.findSingle(checkout_page_body_xpath)
        except:
            break
        try:
            sorry = robot.findSingle(unavailable_xpath)
        except:
            robot.makeSound()
            break


robot = Bot("https://sameday.costco.com/store/checkout_v3", webdriver.Chrome('./driver/chromedriver.exe'))
# check the user has logged in
try:
    robot.wait(after_login_delivery_time_xpath)
except:
    sys.exit()
main()
