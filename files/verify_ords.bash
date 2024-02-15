#
# Verification of ORDS REST API
#
URL=https://myautonomous.adb.eu-frankfurt-1.oraclecloudapps.com
USER=demouser03
curl -i -X POST -d '{"kmh":33}' -H 'Content-Type: application/json' \
        ${URL}/ords/${USER}/wsapi/kmh
#
# Add a new record to the logdata table
# Two versions
#
curl -i -X POST -d '{"kmh":34,"temp":17}' -H 'Content-Type: application/json' \
        ${URL}/ords/${USER}/wsapi/tempkmh
curl -i -X POST -d '{"temp":18}' -H 'Content-Type: application/json' \
        ${URL}/ords/${USER}/wsapi/temp
#
#  Test for the micropyton envrionment, without Content type
#
curl -i -X POST -d '{"temp":5}'  \
        ${URL}/ords/${USER}/wsapi/temp
#
# Fetch the 25 latest samplings
#
curl  -X GET -H 'Content-Type: application/json' \
        ${URL}/ords/${USER}/wsapi/tempkmh | jq '.'
#
# Perform a prediction
#
curl  -X GET -H 'Content-Type: application/json' \
        ${URL}/ords/${USER}/wsapi/predict?temp=32&speed=85 | jq '.'

