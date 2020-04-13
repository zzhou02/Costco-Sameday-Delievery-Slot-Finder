#### Quick-Links
- [Note](#Note)
- [Disclaimer](#Disclaimer)
- [Compatibility](#Compatibility)
- [Download & Usage](#Download)
- [Tips](#Tips)
- [How this works](#How-this-works)

# Costco-Sameday-Delievery-Slot-Finder
A tool that finds available delivery slots for Costco Sameday Delivery in the food department (powered by instacart)

## Note
The COVID-19 pandemic is evolving rapidly, and the trend of online grocery shopping comes to a peak, which makes it nearly impossible to find an open delivery slot. My intention in providing this tool is to lower people's risk of being exposed to the virus due to neccessary grocery shopping. The idea came to me when my mom complained that she had been trying unsuccesfully for several days to get grocery delivery slots.

## Disclaimer
The program doesn't steal your information at all. There is no ip or location detection, and your information will not be leaked because of this program. 

## Compatibility
The programs have only been tested on Windows 10 64 bits machine.<br/>
MacOS and Linux are not supported yet, but may be updated soon.<br/>
Support for Firefox is now added!!<br/>
Note: Chrome version 81/Firefox version > 60 is needed in order to assure the functionality of the program.

## Download
The application currently only supports Windows.
- [Chrome](https://github.com/zzhou02/Costco-Sameday-Delievery-Slot-Finder/releases/download/v1.0/costco_windows_chrome.zip)
- [Firefox-win32](https://github.com/zzhou02/Costco-Sameday-Delievery-Slot-Finder/releases/download/v1.0/costco_windows32_firefox.zip)
- [Firefox-win64](https://github.com/zzhou02/Costco-Sameday-Delievery-Slot-Finder/releases/download/v1.0/costco_windows64_firefox.zip)

## Usage
First and foremost, have your costco sameday delivery cart ready to go.<br/>
Important: this program only works for the [sameday delivery](https://sameday.costco.com/store/costco/storefront). This service should be under “Food, Household, Pet” department. Please check we are talking about the same service.<br/>
Unzip the downloaded zip file and double-click the binary file (the one with “.exe” entension) and it should start running in a few seconds. 

### Start the program
Find the file that is binary file (with exe entension) and double-click.<br/>
After the program started running, enter zip code and log in as usual (Your information is safe).<br/>
When a delivery slot is found, a beep will last for 5 seconds to notify you. So be sure to turn up volume.<br/>
Act quickly after the slot is found since the delivery slot could become unavailable in any minute.<br/> 
To close the program simply close the browser and the terminal pop-up.

## Tips
- The program will exit if you haven't finished logging in within two minutes.
- Do not close the terminal pop-up. The program will not work if it's gone. (will be fixed in next release)
- You can minimize the browser and let it run on background. 
- Personally I would suggest you to run the program in the afternoon around 3 or 4 p.m. which is likely when a lot of delivery slot is released. 

## How this works
The clickable execution is created by pyinstaller. With the help of selenium library, this program automatically and constantly refreshes the checkout page every 30 seconds until it finds a delivery slot. This delivery slot is not presevered for you unless you quickly checkout and secure the delivery slot. 
