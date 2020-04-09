#### Quick-Links
- [Note](#Note)
- [Disclaimer](#Disclaimer)
- [Compatibility](#Compatibility)
- [Usage](#Usage)
- [How this works](#How_this_works)

# Costco-Sameday-Delievery-Slot-Finder
A tool that finds available delivery slots for Costco Sameday Delivery in the food department (powered by instacart)

## Note
The COVID-19 pandemic is evolving rapidly, and the trend of online grocery shopping comes to a peak, which makes it nearly impossible to find an open delivery slot. My intention in providing this tool is to lower people's risk of being exposed to the virus due to neccessary grocery shopping. The idea came to me when my mom complained that she had been trying unsuccesfully for several days to get grocery delivery slots.

## Disclaimer
The program doesn't steal your information at all. There is no ip or location detection, and your information will not be leaked because of this program. 

## Compatibility
As the first draft, this program has only been tested on Windows 10 machine with Chrome browser. Theoretically this program should perform normally on MacOS and Linux, but I have not tested it due to the lack of the access to those systems. I would really appreciate if someone gives a feedback after testing on those systems. 
As of right now, it only supports Chrome browser. Support for Firefox will be updated later.

## Usage
First and foremost, have your costco sameday delivery cart ready to go. 
Important: this program only works for the [sameday delivery](https://sameday.costco.com/store/costco/storefront). This service should be under "Food, Household, Pet" department. Please check we are talking about the same service.
This program requires Chrome, Python, chromedriver, selenium and file in this repo to run. If any of these are installed, you may skip that part. 
### Chrome
You can download Chrome [here](https://www.google.com/chrome/)
### Chromedriver
First check your chrome version and download the [chromedriver](https://chromedriver.chromium.org/downloads) for your system. 
### Python 
You can download Python [here](https://www.python.org/downloads/)
### Clone this repo
Then clone this repo to your system by typing in terminal 
```
git clone https://github.com/zzhou02/Costco-Sameday-Delievery-Slot-Finder.git
```
After sucessfully cloning, fill in necessary information in costco.py
### Selenium
Then add selenium dependency to your program by typing 
```
python -m pip install selenium
```
### Start the program
Run the costco.py by typing in the terminal that is at the same folder as the python files
```
python costco.py
```
That's it, the program should be up and running. You can minimize it and let it run on background. When a delivery slot is found, a beep will last for around 5 seconds to notify you. Be sure to act quickly since the delivery slot could be gone any minute. 

## How this works
With the help of selenium library, this program automatically enters zip code and login for you. Then it constantly refresh the checkout page every 30 seconds until it finds a delivery slot. This delivery slot is not presevered for you unless you quickly checkout and secure the delivery slot. 
