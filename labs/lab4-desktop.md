# Lab 4 (desktop) instructions

## Purpose of lab

The purpose of this lab is to update the logdata table either with an Arduino or with a python command-line script.

The Python code demonstrates how to use the ORDS REST API for reading and updating tables/plsql in an Autonomous database with REST.  

## Prerequsite

Completed lab 1  
For the command-line version, grab an environment with Python 3, for Windows like Anaconda or through Windows Linux Subsystem for Linux.
To run the commandline version you need requests and urllib3:

'pip install requests
'pip install urllib3

The Arduino Lab require attaching the Arduino to your laptop for output from the USB port.
One simple tool is Code with Mu  
![https://codewith.mu/](https://codewith.mu/)  


## Command-line instructions

The command-line Python script inserts into either the logdata or current_speed tables, or lists the last 25 records from logdata  
Usage:  
Get the 25 latest records from logdata  
`python simulate.py --url https://<myadb url>/ords/user25/wsapi/temp` 
Create new logdata record with temp and speed  
`python simulate.py --url https://<myadb url>/ords/user25/wsapi/temp --temp 23  --kmh 74` 
Create new logdata record, but apply latest record in current_speed as speed  
`python simulate.py --url https://<myadb url>/ords/user25/wsapi/temp --temp 23` 
Create new record in the current_speed table  
`python simulate.py --url https://<myadb url>/ords/user25/wsapi/temp --speed 75` 

# Arduino instructions

## Purpose of lab

The purpose of this lab is to get a basic understanding and prepare the Circuitpython environment on the ESP32 Microcontroller.
THen we will configure and run the program that post temperatures to the database

## Prerequsite

For the lab you will get an ESP32 Microcontroller, an AHT20 Temperature and Humidity Sensor, and a small I2C (Inter Integrated Circuit) -cable to connect them together.
You must supply your own USB data cable for use between your Laptop/Mac and the USB C plug on the ESP32 board. 

## Instructions

Unpack both boards. Try not to touch the 3x3 mm blank sensor - it will hurt its accuracy if you do.  
The small cable and plugs is easy to damage so, first look at cable and identify the small blank metal pins on the plugs.  Locate the AHT20 text on the sensorboard and with the text oriented in the correct way - Carefully plug one end of the cable into the left white sockets - with the metal pins pointing down.  Then plug the other end into the white socket of the ESP32 controller.

The two plugs on the AHT20 sensor is actually identical, and can be used to daisy chaining multiple sensor.  To reduce failure rate of the cable sockets, try to not remove cable from ESP32.  It is better to unplug at the AHT20 because you have two sockets - one spare if it gets damaged.

Software/Firmware preparations
download Circuitpython
download Adafruit Library Pack

Plug the USB cable into Laptop and ESP32.
The LED lamp on the ESP32 will start displaying different colors.
You should now get a new USB drive on your Laptop.
Put the ESP32 into boot mode by double clicking the button two times with approx 1 second between.  If successfull LED lamp turns Green.  If not - retry until successfull.

You should now get a new USB drive on your Laptop.
Copy the Circuitpython file into the drive. - The ESP32 will then reboot, and the USB drive will return with a new name.
change to the lib directory, and copy the following python libraries from the Adafruit Library pack to lib.


return to main directory on ESP32 drive and copy the supplied led example program led.py to the ESP32.

The ESP32 LED lamp will start blinking red with the frequency of one Hertz.

Start the MU environment - and select CircuitPython as environment.

You can now get a little bit experience with the ESP32 Circuitpython by changing the RGB (Red Green Blue) parameters to values between 0 and 255.  Every time you save file, the ESP32 will run the new version of the program.

You can also copy the lines with RGB and the following delay one or more times, and change the collors and delays - to create more colorfull blink sequences.

Next task is preparing the database in the next lab - then we will return to the ESP32 in a later lab.

Now it is time to try posting to the database.
Copy this program into MU, and decide if you want to use Cegals wifi or your own phone.
modify :
wifi username
wifi password

Modify the URL to point to your database schema.

Save the file to the ESP32, and you should see debug text in the lower window - while the LED will change collors while the program first tries to connect wifi, reads sensor, and then posts to the database.

You can also use your breath to try to warm the sensor, and see if you get a temperature change.

If you unplug the I2C cable from the sensor, the program will go into a test mode where it cycles between different static temperature values. (you sometimes need to restart the ESP32 after plugging/unplugging) by saving the Python program to the ESP32 - or pressing the restart button on the device).

  




