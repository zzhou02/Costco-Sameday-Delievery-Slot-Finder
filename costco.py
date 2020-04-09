from bot import Bot
import winsound
import random
import time

# Please fill in necessary information
zip_number = 00000
email = ""
password = ""

baseUrl = "https://sameday.costco.com/store/checkout_v3"
zip_xpath = '//*[@id="signup-zipcode"]'
zip_button_xpath = '//*[@id="signup-widget"]/div/div[1]/form/button'
email_xpath = '//*[@id="logonId"]'
password_xpath = '//*[@id="logonPassword"]'
login_button_xpath = '//*[@id="LogonForm"]/fieldset/div[5]/input'
unavailable_xpath = '//*[@id="Delivery options"]/div/p/span[1]/span'


def zip():
    robot.input(zip_xpath, zip_number)
    robot.button(zip_button_xpath)


def login():
    robot.wait(email_xpath)
    robot.input(email_xpath, email)
    robot.input(password_xpath, password)
    robot.button(login_button_xpath)


def main():
    zip()
    login()
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
main()
