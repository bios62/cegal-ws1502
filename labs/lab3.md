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

```
#
# Set default speed if not collected realtime 
#
curl -i -X POST -d '{"kmh":33}' -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/kmh
#
# Add a new record to the logdata table
# Two versions
#
curl -i -X POST -d '{"kmh":34,"temp":17}' -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/tempkmh
curl -i -X POST -d '{"temp":18}' -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/temp
#
#  Test for the micropyton envrionment, without Content type
#
curl -i -X POST -d '{"temp":5}'  https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/temp
#
# Fetch the 25 latest samplings
#
curl  -X GET -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/tempkmh | jq '.'
#
# Perform a prediction
#
curl  -X GET -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/predict?temp=32&speed=85 | jq '.'

```
## Test a prediction with python

Edit the script getprediction.pyton and add the correct values for.  

```
atp_url='https://<your ATP URL>'
atp_username='<your username>'
```
