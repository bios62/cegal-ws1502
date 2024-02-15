#!</bin/bash
URL=https://<your ATP URL>
USER=<your user>
curl  -X GET -o logdata.json -H 'Content-Type: application/json' ${URL}/ords/${USER}/wsapi/tempkmh
curl -i -X POST -d '{"kmh":335}' -H 'Content-Type: application/json' ${URL}/ords/${USER}/wsapi/kmh
curl -i -X POST -H 'Content-Type: application/json' -d '{"kmh":336,"temp":4.5}' ${URL}/ords/${USER}/wsapi/tempkmh
curl -i -X POST -H 'Content-Type: application/json' -d '{"temp":15}' ${URL}/ords/${USER}/wsapi/temp
cat logdata.json | jq '.'


