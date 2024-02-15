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
