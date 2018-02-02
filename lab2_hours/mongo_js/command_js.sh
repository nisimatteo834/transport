#!/bin/bash

echo 'Working on Enjoy...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing enjoy.js > enjoy.csv 
echo 'Done'

echo 'Working on Car2Go...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing car2go.js > car2go.csv
echo 'Done'


