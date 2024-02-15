# Lab 2 instructions

## Purpose of lab

The purprose of this lab is to enable ORDS API.
The lab will create the following API:

`POST /wsapi/tempkmh`    insert into logdata, payload: `'{kmh:<current speed>,"temp":<current temp>}'`  
`POST /wsapi/temp`    insert into logdata, payload: `'{"temp":<current temp>}'`, the API adds latest value from current_speed as defautl value for kmh  
`POST /wsapi/kmh`  insert into current_speed, payload: `'{kmh:<current speed>}'` insert new defalt vale for speed, to be consumed by /wsapi/temp  
`GET /wsapi/tempkm` fetches 25 latest records in the logdata table  

## Prerequsite

Complete lab 1

## Instructions

The lab consists of two elements:
- Load the training data into the trip table
- Build the ORDS environment


## Upload training data for machinelearning

Locate the file kjoredataV2.xlsx on your cloned git repo

Run the instructions from ![Instructions](dataload.md)

## Create the ORDS REST Envrionment

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
# Performa prediction
#
curl  -X GET -H 'Content-Type: application/json' https://<my adb url>.adb.eu-frankfurt-1.oraclecloudapps.com/ords/user25/wsapi/predict?temp=32&speed=85 | jq '.'

```

