#### Quick-Links
- [Note](#Note)
- [Disclaimer](#Disclaimer)
- [Compatibility](#Compatibility)
- [Usage](#Usage)
- [Tips](#Tips)
- [How this works](#How-this-works)

# Costco-Sameday-Delievery-Slot-Finder
A tool that finds available delivery slots for Costco Sameday Delivery in the food department (powered by instacart)

## Note
The COVID-19 pandemic is evolving rapidly, and the trend of online grocery shopping comes to a peak, which makes it nearly impossible to find an open delivery slot. My intention in providing this tool is to lower people's risk of being exposed to the virus due to neccessary grocery shopping. The idea came to me when my mom complained that she had been trying unsuccesfully for several days to get grocery delivery slots.

## Disclaimer
The program doesn't steal your information at all. There is no ip or location detection, and your information will not be leaked because of this program. 

## Compatibility
As the first draft, this program has only been tested on Windows 10 machine with Chrome browser. Theoretically this program should perform normally on MacOS and Linux, but I have not tested it due to the lack of the access to those systems. I would really appreciate if someone gives a feedback after testing on those systems.<br/>
As of right now, it only supports Chrome browser. Support for Firefox will be updated later.<br/>
Note: Chrome version 81 is needed in order to assure the functionality of the program.

## Usage
First and foremost, have your costco sameday delivery cart ready to go. 
Important: this program only works for the [sameday delivery](https://sameday.costco.com/store/costco/storefront). This service should be under “Food, Household, Pet” department. Please check we are talking about the same service.
To use this program just clone this repository and double-click costco.exe and it should start running in a few seconds. 
### Clone this repo
Then clone this repo to your system by opening the terminal in where you want the files to be and typing:
```
git clone https://github.com/zzhou02/Costco-Sameday-Delievery-Slot-Finder.git
```
### Start the program
Find the file that is costco.exe and double-click. 
After the program started running, enter zip code and log in as usual (Your information is safe). 
When a delivery slot is found, a beep will last for 5 seconds to notify you. So be sure to turn up volume.
Act quickly after the slot is found since the delivery slot could become unavailable in any minute. 
To close the program simply close the browser and the terminal pop-up.

## Tips
The program will exit if you haven't finished logging in within two minutes.
You can minimize the browser and let it run on background. 
Personally I would suggest you to run the program in the afternoon around 3 or 4 p.m. which is likely when a lot of delivery slot is released. 

## How this works
The clickable execution is created by pyinstaller. With the help of selenium library, this program automatically and constantly refreshes the checkout page every 30 seconds until it finds a delivery slot. This delivery slot is not presevered for you unless you quickly checkout and secure the delivery slot. 
