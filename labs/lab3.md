# Lab 3 instructions

## Purpose of lab

The purprose of this lab is to build and enable ORDS API.
The lab will create the following API:

`POST /wsapi/tempkmh`    insert into logdata, payload: `'{kmh:<current speed>,"temp":<current temp>}'`  
`POST /wsapi/temp`    insert into logdata, payload: `'{"temp":<current temp>}'`, the API adds latest value from current_speed as defautl value for kmh  
`POST /wsapi/kmh`  insert into current_speed, payload: `'{kmh:<current speed>}'` insert new defalt vale for speed, to be consumed by /wsapi/temp  
`GET /wsapi/tempkm` fetches 25 latest records in the logdata table  

## Prerequsite

Complete lab 1

Ensure the predict_consumption PL/SQL procedure was successfully created in lab 2.

## Instructions

The lab gives step by step instruction on how to in build the REST APIs.

## Build ORDS REST API with script

Copy/paste the script create_ords.sql [](../files/create_ords.sql) into dbactions, and run as script, or do the interactive lab

## Create the ORDS REST Envrionment interatively

Run the instructions from ![Instructions](ords.md)

## Verification of the ORDS REST API with curl

There is a prebuilt script [verify_ords.bash])../files/verify_ords.bash) that can be used for verification  
Edit the lines with correct values:  

```
URL=https://myautonomous.adb.us-phoenix-1.oraclecloudapps.com
USER=demouser03
```

## Test a prediction with python

Edit the script getprediction.pyton and add the correct values for.  

```
atp_url='https://<your ATP URL>'
atp_username='<your username>'
```
