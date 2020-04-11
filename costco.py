from bot import Bot
import winsound
import random
import time

baseUrl = "https://sameday.costco.com/store/checkout_v3"
after_login_delivery_time_xpath = '//*[@id="header"]/div/div/div[5]/div[2]/span/a'
unavailable_xpath = '//*[@id="react-views-container"]/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/h1'

def main():
    while True:
        robot.base()
        robot.pause()
        # if the sorry message is not found we know that a delivery slot is found
        try:
            sorry = robot.findSingle(unavailable_xpath)
        except:
            robot.makeSound()
            break


robot = Bot("https://sameday.costco.com/store/checkout_v3")
robot.wait(after_login_delivery_time_xpath)
print("login success")
main()
